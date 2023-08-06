import numpy as np
from typing import List, Tuple
coord2d = Tuple[float, float]

class VirtualDisplay():
    '''
    The virtual display organises centering of the display
    to the car and transformation from real world to display
    coordinates.
    '''

    def __init__(self, real_width: float, display_size: coord2d):
        self.scale_factor = display_size[0] / real_width
        self.cam_x: float = 0.0
        self.cam_y: float = 0.0
        self.real_width: float = 0.0
        self.real_height: float = 0.0
        real_size = (real_width, display_size[1] / self.scale_factor)
        self.real_width, self.real_height = real_size
        self.screen_width: float = 0.0
        self.screen_height: float = 0.0
        self.screen_width, self.screen_height = display_size
        self.v_camx: float = 0.0
        self.v_camy: float = 0.0

    def _get_virtual_disp_coords(self, real_x: float, real_y: float) -> coord2d:
        '''
        Converts the real world x, y coordinates to internal
        coordinates on (-1, +1)x(-1, +1) space.
        '''
        real_x = real_x - self.cam_x
        real_y = real_y - self.cam_y
        relative_x = 2.0 * (real_x / self.real_width)
        relative_y = 2.0 * (real_y / self.real_height)
        virt_x = relative_x + self.v_camx
        virt_y = relative_y + self.v_camy
        return virt_x, virt_y

    def get_real_pos(self, screen_x: float, screen_y: float) -> coord2d:
        screen_x = 2.0*(screen_x / self.screen_width)-1.0
        screen_y = 2.0*(screen_y / self.screen_height)-1.0
        # Transform to virtual coordinates
        relative_x = screen_x - self.v_camx
        relative_y = screen_y - self.v_camy
        real_x = relative_x * (self.real_width / 2.0) + self.cam_x
        real_y = relative_y * (self.real_height / 2.0) + self.cam_y
        # map (0, 1)^2 to (-1, +1)^2
        #test:
        #scr_x, scr_y = self.get_coords(real_x, real_y)
        #dist = abs(scr_x - screen_x) + abs(scr_y - screen_y)
        #if dist > 1e-10:
        #    print('Get xposition: {:2.3f}, expected {:2.3f}'.format(scr_x, screen_x))
        #    print('Get yposition: {:2.3f}, expected {:2.3f}'.format(scr_y, screen_y))
        #    raise ValueError('Get real position does not work') 
        return real_x, real_y

    def set_vcampos(self, vcamx:float, vcamy:float):
        self.v_camx = vcamx
        self.v_camy = vcamy

    def set_campos(self, cam_x: float, cam_y: float):
        self.cam_x = cam_x
        self.cam_y = cam_y

    def get_coords(self, real_x: float, real_y: float) -> coord2d:
        rel_x, rel_y = self._get_virtual_disp_coords(real_x, real_y)
        # Map (-1, +1) x (-1, +1) to (0, 0)
        screen_rel_x = (rel_x + 1.0) * 0.5
        screen_x = self.screen_width * screen_rel_x
        screen_rel_y = (1.0 - rel_y) * 0.5
        screen_y = self.screen_height * screen_rel_y
        return screen_x, screen_y

    def is_onscreen(self, real_x: float, real_y: float):
        '''
        Compute whether the coordinate is on display
        '''
        screen_x, screen_y = self.get_coords(real_x, real_y)
        x_on = np.logical_and(screen_x >= 0.0, screen_x <= self.screen_width)
        y_on = np.logical_and(screen_y >= 0.0, screen_y <= self.screen_height)
        return np.logical_and(x_on, y_on)

    def get_visible_rw_box(self) -> np.ndarray:
        coord0 = self.get_real_pos(0, 0)
        #coord1 = self.get_real_pos(0, self.screen_height)
        #coord2 = self.get_real_pos(0, 0)
        coord3 = self.get_real_pos(self.screen_width, self.screen_height)
        out_vec = np.zeros(4)
        out_vec[0:2] = coord0
        out_vec[2:4] = coord3
        return out_vec

    def get_visible_bboxs(self, bbox_arr: np.ndarray) -> List[bool]:
        '''
        bbox_arr contains 4 enties x0, y0, x1, y1
        in each row. It is checked if the visible screen area intersects
        with the rectangle in each row.
        '''
        #num = bbox_arr.shape[0]
        x0_arr = bbox_arr[:, 0]
        y0_arr = bbox_arr[:, 1]
        x1_arr = bbox_arr[:, 2]
        y1_arr = bbox_arr[:, 3]
        # cx_arr = np.mean(bbox_arr[:, 0:2], axis=0)
        # cy_arr = np.mean(bbox_arr[:, 2:4], axis=0)
        # c_arr = np.zeros((num, 2))
        # c_arr[:, 0] = cx_arr
        # c_arr[:, 1] = cy_arr
        # w_arr = np.abs(x1_arr - x0_arr)
        # h_arr = np.abs(y1_arr - y0_arr)
        x0, y0, x1, y1 = self.get_visible_rw_box()
        cx, cy = 0.5*(x0+x1), 0.5*(y0+y1)
        # c = np.array([cx, cy])
        # rad_arr = np.sqrt(np.sum((c_arr - tl_arr)**2.0, axis=0))
        # rad = np.linalg.norm(c - np.array([x0, y0]))
        # c_dist = np.sqrt(np.sum((c_arr - c)**2.0, axis=0))
        w, h = abs(x1 - x0), abs(y1 - y0)
        w_arr = np.abs(x1_arr - x0_arr)
        h_arr = np.abs(y1_arr - y0_arr)
        check1_arr = ((x0_arr + 0.5*w_arr) - (x0 + 0.5*w))*2.0 < (w_arr + w)
        check2_arr = ((y0_arr + 0.5*h_arr) - (y0 + 0.5*h))*2.0 < (h_arr + h)
        return np.logical_and(check1_arr, check2_arr)

class VirtualDisplayRot(VirtualDisplay):
    '''
    Virtual display with support of rotating frames.
    '''

    def __init__(self, real_width: float, display_size: coord2d):
        super().__init__(real_width, display_size)
        self.cam_angle: float = 0.0
        self.offset_angle: float = 0.0

    def set_offset_angle(self, offset_angle: float):
        self.offset_angle = offset_angle

    def set_campos(self, cam_x: float, cam_y: float, cam_angle=None):
        super().set_campos(cam_x, cam_y)
        if cam_angle is not None:
            self.cam_angle = cam_angle

    def _get_camrot_coords(self, real_x: float, real_y: float, rot=None):
        '''
        Get position in coordinates rotated about the camera
        '''
        if rot is None:
            total_angle = -self.cam_angle + self.offset_angle
        else:
            total_angle = rot
        angle_sin = np.sin(total_angle)
        angle_cos = np.cos(total_angle)
        # Translate the point
        real_x2 = real_x - self.cam_x
        real_y2 = real_y - self.cam_y
        new_x = (real_x2 * angle_cos - real_y2 * angle_sin) + self.cam_x
        new_y = (real_x2 * angle_sin + real_y2 * angle_cos) + self.cam_y
        return new_x, new_y

    def _get_inverse_camrot_coords(self, pos_x: float, pos_y: float):
        iangle = self.cam_angle - self.offset_angle
        return self._get_camrot_coords(pos_x, pos_y, iangle)

    def _get_virtual_disp_coords(self, real_x: float, real_y: float) -> coord2d:
        '''
        Convert virtual coordinates to on_screen coordinates
        '''
        new_x, new_y = self._get_camrot_coords(real_x, real_y)
        out_x, out_y = super()._get_virtual_disp_coords(new_x, new_y)
        return out_x, out_y

    def get_real_pos(self, screen_x: float, screen_y: float) -> coord2d:
        out_x, out_y = super().get_real_pos(screen_x, screen_y)
        return self._get_inverse_camrot_coords(out_x, out_y)

    def get_total_angle(self):
        return -self.cam_angle + self.offset_angle
