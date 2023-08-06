import os
from .game_object import GameObject
import pygame
from pygame.surface import Surface


class RaceCar(GameObject):

    def __init__(self, pos_x: float, pos_y: float):
        # Define the width and height in real world units
        super().__init__(pos_x, pos_y)
        self.width = 2.2
        self.length = 5.0
        self.data_dir = os.path.join('..', '..', 'Data')
        self.img_path = os.path.join(self.data_dir, 'images', 'car_topview.png')
        self.img_car = pygame.image.load(self.img_path).convert_alpha()
        self.img_rect: pygame.Rect = self.img_car.get_rect()
        self.vel_x: float = 0.0
        self.vel_y: float = 0.0

    def render(self, surface: Surface):
        print('Implement RaceCar render')
