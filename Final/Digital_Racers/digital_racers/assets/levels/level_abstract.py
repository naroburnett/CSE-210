from pickle import NONE
from constants import *


class Level_Abstract:
    def __init__(self):
        self.game_mode = None
        self.player_1_car = None
        self.player_2_car = None
        self.track = None
        self.track_border = None
        self.track_border_mask = None
        self.finish = None
        self.finish_mask = None
        self.finish_position = None
        self.ground = None

    def set_game_mode(self, game_mode):
        self.game_mode = game_mode

    def set_player_1_car(self, img, scale):
        self.player_1_car = scale_image(pygame.image.load(img), 0.55)
    
    def set_player_2_car(self, img, scale):
        self.player_2_car = scale_image(pygame.image.load(img), 0.55)
    
    def set_track(self, png):
        self.track = scale_image(pygame.image.load(png), 0.9)
    
    def set_track_border(self, png, scale):
        self.track_border = scale_image(pygame.image.load(png), 0.9)

    def set_track_border_mask(self):
        self.track_border_mask = pygame.mask.from_surface(self.track_border)
    
    def set_finish(self, png):
        self.finish = pygame.image.load(png)
    
    def set_finish_mask(self):
        self.finish_mask = pygame.mask.from_surface(self.finish)
    
    def set_finish_position(self, pos_x, pos_y):
        self.finish_position = (pos_x, pos_y)
    
    def set_ground(self, ground, scale):
        self.ground = scale_image(pygame.image.load(ground), 2.5)
    
    def get_game_mode(self):
        return self.game_mode 

    def get_player_1_car(self):
        return self.player_1_car
    
    def get_player_2_car(self):
        return self.player_2_car
    
    def get_track(self):
        return self.track
    
    def get_track_boarder(self):
        return self.track_border

    def get_track_boarder_mask(self):
        return self.track_border_mask
    
    def get_finish(self):
        return self.finish
    
    def get_finish_mask(self):
        return self.finish_mask
    
    def get_finish_position(self):
        return self.finish_positon
    
    def get_ground(self):
        return self.ground
