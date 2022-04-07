import pygame
import math
from constants import *


class Vehicle:
    def __init__(self, max_vel, rotation_vel):
        self.vehicle = None
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.acceleration = 0.1
        self.start_pos = (0,0)
        self.x, self.y = (0,0)
        self.control_type = 2
        self.player_name = ""

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.vehicle, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.vehicle)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self):
        self.x, self.y = self.start_pos
        self.angle = 0
        self.vel = 0
    
    def set_vehicle(self, img):
        self.vehicle = img
    
    def get_vehicle(self):
        return self.vehicle
    
    def set_max_vel(self, max):
        self.max_vel = max
    
    def get_max_vel(self):
        return self.max_vel
    
    def set_rotation_vel(self, max):
        self.rotation_vel = max
    
    def get_rotation_vel(self):
        return self.rotation_vel
    
    def set_start_pos(self, pos):
        self.start_pos = pos
        self.x, self.y = pos
    
    def set_control_type(self, type):
        self.control_type = type
    
    def set_player_name(self, name):
        self.player_name = name

    def get_player_name(self):
        return self.player_name

    def get_control_type(self):
        return self.control_type
    