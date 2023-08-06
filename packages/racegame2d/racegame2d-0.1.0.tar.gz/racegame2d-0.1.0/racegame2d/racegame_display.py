import pygame
from track_model.track import Track
import numpy as np
import os
import cv2
import subprocess
from typing import Tuple, List
from .trackpiece import TrackPiece
from .virtual_display import VirtualDisplay, VirtualDisplayRot
from track_model.finite_line import FiniteLineGroup, FiniteLine


coord2d = Tuple[float, float]
os.environ["SDL_VIDEODRIVER"] = "dummy"


class RacecarDisplay():

    def __init__(self, track: Track, res: int, fig_w=None):
        # Setup the track
        self.track: Track = track
        self.figure_shape = (-1.0, -1.0) #  is overwritten in setup_track
        self.track_pieces: List[TrackPiece] = []
        self.bboxs: np.ndarray = None
        self.figure_shape = self.get_figshape(res, fig_w)
        self.load_track(track)
        self.data_shape = self.figure_shape
        self.rw_width = 200.0
        #print('Using real world window width: ', self.rw_width)
        self.v_disp = VirtualDisplayRot(self.rw_width, display_size=self.figure_shape)
        self.v_disp.set_offset_angle(0.5*np.pi)
        self.v_disp.set_vcampos(0.0, -0.6667)
        # Setup the display
        pygame.init()
        self.display = pygame.display.set_mode(self.figure_shape)
        pygame.display.set_caption('Racecar Display by Christoph Hoeppke v0.0.2')
        self.car_img = pygame.image.load('../../Data/images/car_topview.png')
        self.car_img_other = pygame.image.load('../../Data/images/car_topview_other.png')
        self.car_img = self.car_img.convert_alpha()
        self.car_img_other = self.car_img_other.convert_alpha()
        self.car_real_size = (4.56, 1.88)
        car_size = self.get_screen_size(*self.car_real_size)
        self.car_size_px = car_size
        self.car_img = pygame.transform.scale(self.car_img, car_size)
        self.car_img_other = pygame.transform.scale(self.car_img_other, car_size)
        # Setup the racetrack
        self.clock = pygame.time.Clock()
        self.textmk = pygame.font.SysFont('Ubuntu', 16)
        self.verbose = False

    def load_track(self, track: Track):
        self.track = track
        '''
        Call in the constructor to initialize trackpieces.
        '''
        self.track_pieces: List[TrackPiece] = []
        track_len = track.get_length()
        num_pos = int(round(track_len / 5.0))
        pos_list = np.linspace(0.001, track_len-0.001, num=num_pos)
        pos_list = [track.get_point(s) for s in pos_list]
        pos_list = list(zip(pos_list[0:-1], pos_list[1:]))
        num_elements = len(pos_list)
        self.bboxs = np.zeros((num_pos, 4, 2), dtype=np.float64)
        for idx, (p0, p1) in enumerate(pos_list):
            # Crate a new track piece
            finish = True if idx == num_pos-1 else False
            new_piece = TrackPiece(p0, p1, track.get_width())
            new_piece.init_finish(is_finish=finish)
            new_piece._show_triangle = (idx % 5 == 0)
            self.track_pieces.append(new_piece)
            self.bboxs[idx,: ,:] = new_piece.get_bound_box()

    def get_track_bounds(self, track: Track):
        track_len = track.get_length()
        track_width = track.get_width()
        samples_x = []
        samples_y = []
        # Gather samples of points on the track
        for track_dist in track.hb_sdists:
            track_point = track.get_point(track_dist)
            left_ = track_point.get_bound(track_width, which='left')
            right_ = track_point.get_bound(track_width, which='right')
            for point in [left_, right_]:
                samples_x.append(point.pos_x)
                samples_y.append(point.pos_y)
        return samples_x, samples_y

    def set_data_shape(self, data_h: int):
        data_w = int(round(16*data_h/9))
        self.data_shape = (data_w, data_h)

    def get_figshape(self, figure_height: float, figure_width=None):
        '''
        Called in the constructor of a Racecar Display. Used to
        setup the required scaling for the track.
        '''
        # Compute figure scale
        figure_height = int(round(figure_height))
        if figure_width is None:
            figure_width = int(round(figure_height * 16 / 9))
        return (figure_width, figure_height)

    def get_screen_size(self, real_w: float, real_h: float):
        '''
        Scales a track object to the appropriate size in screen coordinates.
        '''
        scale_factor = self.v_disp.scale_factor
        img_w = int(round(real_w*scale_factor))
        img_h = int(round(real_h*scale_factor))
        return (img_w, img_h)

    def get_screen_coordinates(self, pos_x: float, pos_y: float):
        '''
        converts a tuple of track coordinates to screen coordinates.
        '''
        return self.v_disp.get_coords(pos_x, pos_y)

    def render_car(self, car_x, car_y, car_angle, is_other=False):
        # Render the car
        car_img = self.car_img
        if is_other:
            car_img = self.car_img_other
        car_rotation_ang = np.rad2deg(car_angle+self.v_disp.get_total_angle())
        rot_car_img = pygame.transform.rotate(car_img, car_rotation_ang)
        car_pos = self.get_screen_coordinates(car_x, car_y)
        car_width, car_height = self.car_size_px
        car_rect = rot_car_img.get_rect()
        car_rect.center = car_pos
        tl_pos = car_rect.topleft
        self.display.blit(rot_car_img, tl_pos)

    def render_car_rays(self, car_x, car_y, ray_angles, ray_lengths):
        '''
        Render lines indicating the car distance to boundary on track.
        '''
        num_rays = len(ray_angles)
        for i in range(num_rays):
            ray_len = ray_lengths[i]
            ray_angle = ray_angles[i]
            ray_start_x = car_x
            ray_start_y = car_y
            ray_end_x = car_x + ray_len * np.cos(ray_angle)
            ray_end_y = car_y + ray_len * np.sin(ray_angle)
            ray_start = self.get_screen_coordinates(ray_start_x, ray_start_y)
            ray_end = self.get_screen_coordinates(ray_end_x, ray_end_y)
            pygame.draw.line(self.display, (200, 20, 20), ray_start, ray_end, width=2)

    def render_track_bound(self, bound: FiniteLineGroup):
        high_color = (220, 50, 50)
        low_color = (220, 220, 220)
        for idx, line in enumerate(bound.line_group):
            line_start = self.get_screen_coordinates(*line.start)
            line_end = self.get_screen_coordinates(*line.end)
            if idx % 2 == 0:
                color = low_color
            else:
                color = high_color
            pygame.draw.line(self.display, color, line_start, line_end, width=2)

    def update_display(self, car_x, car_y, car_angle, track_angle, stats_dict=None):
        '''
        update the pygame display with the car at new position.
        '''
        # Update the virtual camera position.
        self.v_disp.set_campos(car_x, car_y, car_angle)
        # Setup a green background.
        # color_grass = (20, 140, 20)
        color_grass = (140, 140, 140)
        self.display.fill(color_grass)
        num_elements = self.bboxs.shape[0]
        #
        # Compute if elements are on screen
        on_screen = np.repeat(False, num_elements)
        for cidx in range(4):
            cpos_x = self.bboxs[:, cidx, 0]
            cpos_y = self.bboxs[:, cidx, 1]
            cpos_x_scr, cpos_y_scr = self.v_disp.get_coords(cpos_x, cpos_y)
            c_on_screen_x = np.logical_and(cpos_x_scr >= -20.0, cpos_x_scr <= 20.0 + self.display.get_width())
            c_on_screen_y = np.logical_and(cpos_y_scr >= -20.0, cpos_y_scr <= 20.0 + self.display.get_height())
            on_screen = np.logical_or(on_screen, np.logical_and(c_on_screen_x, c_on_screen_y))
        on_screen = np.logical_or(on_screen[0:-1], on_screen[1:])
        num_on_screen = np.sum(on_screen)
        if self.verbose:
            print('Found {} of {} elements on screen'.format(num_on_screen, num_elements))
        #x_arr, y_arr = self.v_disp.get_coords(self.bboxs[:, 0], self.bboxs[:, 3])
        # on_screen = self.v_disp.is_onscreen(x_arr, y_arr)
        # print('Drawing {:d} track pieces'.format(np.sum(on_screen)))
        # check the intersections
        on_screen_pieces = [self.track_pieces[i] for i in range(len(on_screen)) if on_screen[i]]
        for piece in on_screen_pieces:
            piece.render(self.display, self.v_disp)
        self.render_car(car_x, car_y, car_angle)
        if stats_dict is not None:
            self.write_stats(stats_dict)
        if self.verbose:
            print('Display updated')

    def write_stats(self, stats_dict):
        last_hight: int = 5
        for key in stats_dict:
            val = stats_dict[key]
            new_str = '{key}: {val}'.format(key=key, val=val)
            text_surface = self.textmk.render(new_str, True, (0, 0, 0))
            self.display.blit(text_surface, (5, last_hight))
            last_hight += text_surface.get_size()[1] + 2

    def flip(self):
        pygame.display.flip()

    def save_frame(self, fname: str):
        '''
        Save the current frame to file.
        '''
        pygame.image.save(self.display, fname)

    def make_movie(self, fps: float=60.0, fname: str='movie.mp4'):
        '''
        Calls ffmpeg to make a movie from the figs directory.
        '''
        if not os.path.isdir('./figs'):
            os.mkdir('./figs/')
        cmd = 'ffmpeg'
        params = [cmd]
        params.append('-y')
        params.append('-framerate')
        params.append(str(fps))
        params.append('-i')
        params.append('./figs/frame_%04d.png')
        params.append('{}'.format(fname))
        cmd = cmd.format(fps)
        p = subprocess.run(params)
        print('\n')
        print('Created movie')

    def clear_figs_folder(self):
        figs_folder = os.path.join('.', 'figs')
        # Clear the figs directory
        for fname in os.listdir(figs_folder):
            fpath = os.path.join(figs_folder, fname)
            if os.path.isfile(fpath):
                os.remove(fpath)

    def get_image_data(self, rgb: bool=False):
        imgdata = pygame.surfarray.array3d(self.display)
        imgdata.swapaxes(0, 1)
        fig_w, fig_h = self.figure_shape
        shape_rgb = (fig_w, fig_h, 3)
        shape_bw = (fig_w, fig_h)
        # frame = np.zeros(shape_rgb, np.float32)
        frame = imgdata.astype(np.float32)
        # Reshape data
        if not rgb:
            # Convert to BW
            frame = np.mean(frame, axis=2)
        if self.figure_shape != self.data_shape:
            fw, fh = self.data_shape
            frame = cv2.resize(frame, (fh, fw))
        return frame.astype(np.uint8)

class RacecarDisplayBuffered(RacecarDisplay):
    '''
    Normal the normal RacecarDisplay does not support tracking
    of multiple frames in memory. This class saves a finite
    number of frames for later computations.
    '''

    def __init__(self, track: Track, width: int=800, nframes: int=8):
        super().__init__(track, width=width)
        self.num_stored_frames = nframes
        self.frame_idx: int = 0
        fig_width, fig_height = self.figure_shape
        self.frame_buffer = np.zeros((fig_width, fig_height, 3, nframes))

    def update_display(self, car_x, car_y, car_angle, track_angle, stats_dict=None):
        super().update_display(car_x, car_y, car_angle, track_angle, stats_dict)
        imgdata = pygame.surfarray.array3d(self.display)
        imgdata.swapaxes(0, 1)
        self.frame_buffer[:, :, :, self.frame_idx] = imgdata
        self.frame_idx = (self.frame_idx + 1) % self.num_stored_frames

    def observe_visual(self):
        '''
        Observe the pixel data from display in black and white.
        '''
        last_frames = [] 
        for k in range(self.num_stored_frames):
            fidx = self.frame_idx - k
            last_frames.append(self.frame_buffer[:, :, :, fidx])
        frames_out = []
        for frame in last_frames:
            bw_frame = np.mean(frame/255.0, axis=2)
            frames_out.append(bw_frame)
        return np.concatenate([frames_out])
