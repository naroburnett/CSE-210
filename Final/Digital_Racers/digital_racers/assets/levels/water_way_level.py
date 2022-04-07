import pygame
from assets.levels.level_abstract import Level_Abstract
from constants import *

class Water_Way_Level(Level_Abstract):
    def __init__(self):
        super().__init__()
    
    def set_level_properties(self, game_mode):
        self.set_game_mode(game_mode)
        self.set_track("digital_racers/assets/images/water_ground.jpg", 2.5)
        self.set_track_border("digital_racers/assets/images/race_track-border.png", 0.9)
        self.set_track_border_mask()
        self.set_finish("digital_racers/assets/images/water_way_finish.png", 0.087)
        self.set_finish_mask()
        self.set_finish_position(130, 250)
        self.set_ground("digital_racers/assets\images\water_ground.jpg", 2.5)
        self.set_vehicle_list(['green','grey','purple','yellow'])
        self.set_vehicel_type('Duck')
        self.set_player_1_start_pos(180, 200)
        self.set_player_2_start_pos(150, 200)
        self.set_bot_path([(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
        (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)])

    def select_vehicle(self, color):

        if color == "green":
            vehicle = scale_image(pygame.image.load("digital_racers/assets/images/green-duck.png"), 0.03)
            return vehicle
        
        if color == "grey":
            vehicle = scale_image(pygame.image.load("digital_racers/assets/images/grey-duck.png"), 0.03)
            return vehicle
        
        if color == "purple":
            vehicle = scale_image(pygame.image.load("digital_racers/assets/images/purple-duck.png"), 0.03)
            return vehicle
        
        if color == "yellow":
            vehicle = scale_image(pygame.image.load("digital_racers/assets/images/yellow-duck.png"), 0.03)
            return vehicle