import pygame
from pickle import NONE
from constants import *


class Level_Abstract:
    def __init__(self):
        self.game_mode = None
        self.player_1_type = None
        self.player_2_type= None
        self.track = None
        self.track_border = None
        self.track_border_mask = None
        self.finish = None
        self.finish_mask = None
        self.finish_position = None
        self.ground = None
        self.vehicle_list = []
        self.vehicle_type = None
        self.player_1_start_pos = None
        self.player_2_start_pos = None
        self.bot_path = []

    def set_game_mode(self, game_mode):
        self.game_mode = game_mode

    def set_player_1_car(self, img, scale):
        self.player_1_car = scale_image(pygame.image.load(img), scale)
    
    def set_player_2_car(self, img, scale):
        self.player_2_car = scale_image(pygame.image.load(img), scale)
    
    def set_track(self, png, scale):
        self.track = scale_image(pygame.image.load(png), scale)
    
    def set_track_border(self, png, scale):
        self.track_border = scale_image(pygame.image.load(png), scale)

    def set_track_border_mask(self):
        self.track_border_mask = pygame.mask.from_surface(self.track_border)
    
    def set_finish(self, png, scale = 0 ):
        self.finish = scale_image(pygame.image.load(png), scale)
    
    def set_finish_mask(self):
        self.finish_mask = pygame.mask.from_surface(self.finish)
    
    def set_finish_position(self, pos_x, pos_y):
        self.finish_position = (pos_x, pos_y)
    
    def set_ground(self, ground, scale):
        self.ground = scale_image(pygame.image.load(ground), scale)
    
    def set_vehicle_list(self, list):
        self.vehicle_list = list
    
    def set_vehicel_type(self, type):
        self.vehicle_type = type
    
    def set_player_types(self):
        if self.game_mode == 1:
            self.player_1_type = "player"
            self.player_2_type = "player"

        elif self.game_mode == 2:
            self.player_1_type = "player"
            self.player_2_type = "bot"

    def set_player_1_start_pos(self, pos_x, pos_y):
        self.player_1_start_pos = (pos_x, pos_y)
    
    def set_player_2_start_pos(self, pos_x, pos_y):
        self.player_2_start_pos = (pos_x, pos_y)
    
    def set_bot_path(self, path):
        self.bot_path = path
    
    def set_players_type(self):
        if self.game_mode == 1:
            self.player_1_type = 1
            self.player_2_type = 1
        
        elif self.game_mode == 2:
            self.player_1_type = 1
            self.player_2_type = 2

    def get_game_mode(self):
        return self.game_mode 

    def get_player_1_car(self):
        return self.player_1_car
    
    def get_player_2_car(self):
        return self.player_2_car
    
    def get_track(self):
        return self.track
    
    def get_track_border(self):
        return self.track_border

    def get_track_border_mask(self):
        return self.track_border_mask
    
    def get_finish(self):
        return self.finish
    
    def get_finish_mask(self):
        return self.finish_mask
    
    def get_finish_position(self):
        return self.finish_position
    
    def get_ground(self):
        return self.ground
    
    def get_vehicle_list(self):
        return self.vehicle_list
    
    def get_vehicle_type(self):
        return self.vehicle_type
    
    def get_player_1_start_pos(self):
        return self.player_1_start_pos
    
    def get_player_2_start_pos(self):
        return self.player_2_start_pos

    def get_bot_path(self):
        return self.bot_path
    
    def get_player_one_type(self):
        return self.player_1_type

    def get_player_two_type(self):
        return self.player_2_type

    def select_vehicle(self, color):
        pass

    def set_level_properties(self, game_mode):
        pass

    def print_level_properties(self):
        print(self.game_mode)
        print(self.player_1_car)
        print(self.player_2_car)
        print(self.track)
        print(self.track_border)
        print(self.track_border_mask)
        print(self.finish)
        print(self.finish_mask)
        print(self.finish_position)
        print(self.ground)
        print(self.vehicle_list)
        print(self.vehicle_type)
