from game.actors.vehicle import Vehicle
from constants import *

class Player(Vehicle):

    def __init__(self, max_vel, rotation_vel):
        super().__init__(max_vel, rotation_vel)
        
    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel
        self.move()
