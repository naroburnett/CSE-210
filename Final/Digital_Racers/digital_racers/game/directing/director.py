import pygame
from constants import *
from game.actors.game_info import GameInfo
from game.script.game_logic import Game_logic
from random import *

class Director():
    def __init__(self, Player_One, Player_Two, Level, Images):
        self.player_one = Player_One
        self.player_two = Player_Two
        self.level = Level
        self.images = Images


    def start_game(self):
        run = True
        clock = pygame.time.Clock()
        game_info = GameInfo()

        while run:
            clock.tick(FPS)
            game_logic = Game_logic(WIN, self.images, self.player_one, self.player_two, game_info)
            game_logic.draw(WIN, self.images, self.player_one, self.player_two, game_info)

            while not game_info.started:
                blit_text_center(
                    WIN, MAIN_FONT, f"Press any key to start level {game_info.level}!")
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                    if event.type == pygame.KEYDOWN:
                        game_info.start_level()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            if self.level.get_game_mode() == 1: 
                game_logic.move_player(self.player_one)
                game_logic.move_player(self.player_two)
                pass

            elif self.level.get_game_mode() == 2: 
                game_logic.move_player(self.player_one)
                self.player_two.move()
                pass

            game_logic.handle_collision(self.player_one, self.player_two, game_info, self.level)

            if game_info.game_finished():
                blit_text_center(WIN, MAIN_FONT, "You won the game!")
                pygame.time.wait(5000)
                game_info.reset()
                self.player_one.reset()
                self.player_two.reset()


        pygame.quit()