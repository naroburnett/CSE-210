import pygame
from constants import *


class Game_logic:
    def __init__(self, Win, Images, Player_One, Player_Two, Game_Info):
        self.win = Win
        self.images = Images
        self.player_one = Player_One
        self.player_two = Player_Two
        self.game_info = Game_Info
        



    def draw(self, win, images, player_one, player_two, game_info):
        for img, pos in images:
            win.blit(img, pos)

        level_text = MAIN_FONT.render(
            f"Level {game_info.level}", 1, (255, 255, 255))
        win.blit(level_text, (10, HEIGHT - level_text.get_height() - 70))

        time_text = MAIN_FONT.render(
            f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
        win.blit(time_text, (10, HEIGHT - time_text.get_height() - 40))

        vel_text = MAIN_FONT.render(
            f"Vel: {round(player_one.vel, 1)}px/s", 1, (255, 255, 255))
        win.blit(vel_text, (10, HEIGHT - vel_text.get_height() - 10))

        player_one.draw(win)
        player_two.draw(win)
        pygame.display.update()


    def move_player(self, player):
        if player.get_player_name() == "Player_One":
            keys = pygame.key.get_pressed()
            moved = False

            if keys[pygame.K_a]:
                player.rotate(left=True)
            if keys[pygame.K_d]:
                player.rotate(right=True)
            if keys[pygame.K_w]:
                moved = True
                player.move_forward()
            if keys[pygame.K_s]:
                moved = True
                player.move_backward()

            if not moved:
                player.reduce_speed()

        elif player.get_player_name() == "Player_Two":
            keys = pygame.key.get_pressed()
            moved = False
            
            if keys[pygame.K_j]:
                player.rotate(left=True)
            if keys[pygame.K_l]:
                player.rotate(right=True)
            if keys[pygame.K_i]:
                moved = True
                player.move_forward()
            if keys[pygame.K_k]:
                moved = True
                player.move_backward()

            if not moved:
                player.reduce_speed()
        


    def handle_collision(self, player_one, player_two, game_info, level):
        TRACK_BORDER_MASK = level.get_track_border_mask()
        FINISH_MASK = level.get_finish_mask()
        FINISH_POSITION = level.get_finish_position()
        
        if player_one.collide(TRACK_BORDER_MASK) != None:
            player_one.bounce()

        computer_finish_poi_collide = player_two.collide(
            FINISH_MASK, *FINISH_POSITION)
        if computer_finish_poi_collide != None:
            blit_text_center(WIN, MAIN_FONT, "You lost!")
            pygame.display.update()
            pygame.time.wait(5000)
            game_info.reset()
            player_one.reset()
            player_two.reset()

        player_finish_poi_collide = player_one.collide(
            FINISH_MASK, *FINISH_POSITION)
        if player_finish_poi_collide != None:
            if player_finish_poi_collide[1] == 0:
                player_one.bounce()
            else:
                game_info.next_level()
                player_one.reset()
                if level.get_game_mode() == 2: 
                    player_two.next_level(game_info.level)
        
        if level.get_game_mode() == 1: 
            if player_two.collide(TRACK_BORDER_MASK) != None:
                player_two.bounce()

            computer_finish_poi_collide = player_two.collide(
                FINISH_MASK, *FINISH_POSITION)
            if computer_finish_poi_collide != None:
                blit_text_center(WIN, MAIN_FONT, "You lost!")
                pygame.display.update()
                pygame.time.wait(5000)
                game_info.reset()
                player_two.reset()
                player_one.reset()

            player_finish_poi_collide = player_two.collide(
                FINISH_MASK, *FINISH_POSITION)
            if player_finish_poi_collide != None:
                if player_finish_poi_collide[1] == 0:
                    player_two.bounce()
                else:
                    game_info.next_level()
                    player_two.reset()
                    player_one.next_level(game_info.level)
        # #player one collision
        # if player_one.collide((level.get_track_border())) != None:
        #     player_one.bounce()

        # computer_finish_poi_collide = player_two.collide((level.get_finish_mask()), (level.get_finish_position()))
        # if computer_finish_poi_collide != None:
        #     blit_text_center(WIN, MAIN_FONT, "You lost!")
        #     pygame.display.update()
        #     pygame.time.wait(5000)
        #     game_info.reset()
        #     player_one.reset()
        #     player_two.reset()

        # player_finish_poi_collide = player_one.collide((level.get_finish_mask()), (level.get_finish_position()))
        # if player_finish_poi_collide != None:
        #     if player_finish_poi_collide[1] == 0:
        #         player_one.bounce()
        #     else:
        #         game_info.next_level()
        #         player_one.reset()
        #         player_two.next_level(game_info.level)

        # #player two collision
        # if player_two.collide((level.get_track_border())) != None:
        #     player_two.bounce()

        # computer_finish_poi_collide = player_one.collide((level.get_finish_mask()), (level.get_finish_position()))
        # if computer_finish_poi_collide != None:
        #     blit_text_center(WIN, MAIN_FONT, "You lost!")
        #     pygame.display.update()
        #     pygame.time.wait(5000)
        #     game_info.reset()
        #     player_one.reset()
        #     player_two.reset()

        # player_finish_poi_collide = player_two.collide((level.get_finish_mask()), (level.get_finish_position()))
        # if player_finish_poi_collide != None:
        #     if player_finish_poi_collide[1] == 0:
        #         player_one.bounce()
        #     else:
        #         game_info.next_level()
        #         player_one.reset()
        #         player_two.next_level(game_info.level)