import pygame
from level_abstract import Level_Abstract
from constants import *

class Race_Track_Level(Level_Abstract):
    def __init__(self):
        super().__init__()
    
    def set_level_properties(self, game_mode):
        self.set_game_mode(game_mode)
        self.set_track("digital_racers/assets\images/race_track.png", 0.9)
        self.set_track_border("digital_racers/assets/images/race_track-border.png", 0.9)
        self.set_track_border_mask()
        self.set_finish("digital_racers/assets/images/race_track_finish.png")
        self.set_finish_mask()
        self.set_finish_position(130, 250)
        self.set_ground("digital_racers/assets\images\grass_ground.jpg", 2.5)

