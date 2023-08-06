from . import game_object
from . import trackpiece
from PIL import Image, ImageDraw
from track_model.track import Track
import numpy as np
import tempfile
import os


class GameWorld():

    def __init__(self, track: Track):
        self.screen_width: int = 1280
        self.screen_heigh: int = 720
        self.screen_size = (self.screen_width, self.screen_heigh)
        self.screen = Image.new('RGB', self.screen_size)
        self.renderer = ImageDraw.Draw(self.screen)
        self.done = False
        self.track: Track = track
        self.game_objects: List[GameObject] = []
        self.campos_x: float = 0.0
        self.campos_y: float = 0.0
        self.render_background()
        self.save_img()

    def render_background(self):
        back_color = (40, 200, 50)
        self.renderer.rectangle([(0, 0), self.screen_size], fill=back_color)

    def render_loop(self):
        '''
        Render elements to display.
        '''
        self.render_background()
        # Render all the rectangles on screen.
        for gobj in self.game_objects:
            gobj.render(self.screen, self.renderer)

    def save_img(self):
        '''
        Save the current frame to file.
        '''
        img_folder = os.path.join('.', 'figs')
        if not os.path.exists(img_folder):
            os.mkdir(img_folder)
        img_file = os.path.join(img_folder, 'latest.png')
        # Save as PNG to prevent artifacts
        self.screen.save(img_file, format='PNG')
