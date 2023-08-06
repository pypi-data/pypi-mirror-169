from PIL import Image, ImageDraw
from abc import ABC, abstractmethod


class GameObject():

    def __init__(self, real_x: float, real_y: float):
        self.real_x: float = real_x
        self.real_y: float = real_y
        self.rotation: float = 0.0

    @abstractmethod
    def render(self, img: Image, render: ImageDraw):
        '''
        Abstract method for rendering a game object onto the screen.
        '''
        pass
