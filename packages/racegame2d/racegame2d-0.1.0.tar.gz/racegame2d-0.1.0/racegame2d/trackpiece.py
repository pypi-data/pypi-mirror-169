from . import gameworld
from .game_object import GameObject
from PIL import Image, ImageDraw
from track_model.track import TrackElement, TrackPoint, Point2D
from typing import TYPE_CHECKING, List, Tuple
import pygame
import numpy as np

rgb_tuple = Tuple[int, int, int]

if TYPE_CHECKING:
    from .gameworld import GameWorld
    from .racegame_display import VirtualDisplay
    from .racegame_display import RacecarDisplay

class TrackPiece():
    color_road: rgb_tuple = (45, 45, 45)
    color_finish: rgb_tuple = (200, 20, 20)
    color_triangle: rgb_tuple = (60, 60, 60)

    def __init__(self, start: TrackPoint, end: TrackPoint, width: float):
        # print('New track piece at {} {}'.format(start.get_position().as_tuple(), start.get_orientation(mode='deg')))
        self.start_point: TrackPoint = start
        self.end_point: TrackPoint = end
        self.rw_corners: List[TrackPoint] = []
        self.bbox: np.ndarray = np.zeros((4, 2))
        self.width = width
        self.finish = False
        self._show_triangle = False
        self.color:rgb_tuple = None
        start_point = np.array(self.start_point.get_position().as_tuple())
        end_point = np.array(self.end_point.get_position().as_tuple())
        self.length = np.linalg.norm(end_point - start_point)
        self.init_corners()
        self.init_finish(False)
        self.init_triangle()

    def init_finish(self, is_finish=False):
        self.finish = is_finish
        if self.finish:
            self.color = TrackPiece.color_finish
        else:
            self.color = TrackPiece.color_road

    def init_corners(self):
        corners = []
        p0, p1 = self.start_point, self.end_point
        track_width = self.width
        corner0 = p0.get_bound(track_width, which='left')
        corner1 = p0.get_bound(track_width, which='right')
        corner2 = p1.get_bound(track_width, which='right')
        corner3 = p1.get_bound(track_width, which='left')
        self.rw_corners = [corner0, corner1, corner2, corner3]
        self.rw_corners = [c.as_tuple() for c in self.rw_corners]
        for idx, corner in enumerate(self.rw_corners):
            self.bbox[idx, :] = corner

    def get_bound_box(self) -> np.ndarray:
        '''
        Get the real world coordinates of the bounding box
        '''
        return self.bbox

    def init_triangle(self):
        '''
        We want to draw a small directional triangle on the track.
        '''
        self.triangle_len = self.length / 5.0
        self.triangle_width = self.width / 8.0
        triangle_base_pos: Point2D = self.start_point.get_position()
        triangle_dir_vec: Point2D = self.start_point.get_direction()
        triangle_base_vec: Point2D = self.start_point.get_ortho_direction()
        c0 = triangle_base_pos + self.triangle_len * triangle_dir_vec
        c1 = triangle_base_pos - self.triangle_width * triangle_base_vec
        c2 = triangle_base_pos + self.triangle_width * triangle_base_vec
        triangle_corners = [c0, c1, c2]
        self.triangle_corners = [c.as_tuple() for c in triangle_corners]

    def need_render(self, v_disp: 'VirtualDisplay'):
        c_on_screen = [v_disp.is_onscreen(*c) for c in self.rw_corners]
        need_render = any(c_on_screen)
        return need_render


    def render(self, display, v_disp: 'VirtualDisplay'):
        '''
        Draw a single track element (if required)
        '''
        self.render_road(display, v_disp)
        if self._show_triangle:
            self.render_triangle(display, v_disp)

    def render_road(self, display, v_disp: 'VirtualDisplay'):
        # Draw the road
        corners = [v_disp.get_coords(*c) for c in self.rw_corners]
        pygame.draw.polygon(display, self.color, corners)
        # Draw the directional triangle

    def render_triangle(self, display, v_disp: 'VirtualDisplay'):
        #if need_render:
        corners = [v_disp.get_coords(*c) for c in self.triangle_corners]
        pygame.draw.polygon(display, TrackPiece.color_triangle, corners)
