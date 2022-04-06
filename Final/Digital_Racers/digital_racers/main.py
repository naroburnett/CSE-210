import pygame
from constants import *
from game.actors.game_info import GameInfo
from game.actors.player import Player
from game.actors.computer_player import Computer_Player
from game.script.game_logic import Game_logic



# ----------------------------------------------------------------------------------------------
# __Main__
# ----------------------------------------------------------------------------------------------

def main():
    run = True
    clock = pygame.time.Clock()
    images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
            (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))]
    player_car = Player(4, 4)
    computer_car = Computer_Player(2, 4, PATH)
    game_info = GameInfo()

    while run:
        clock.tick(FPS)
        game_logic = Game_logic(WIN, images, player_car, computer_car, game_info)
        game_logic.draw(WIN, images, player_car, computer_car, game_info)

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

        game_logic.move_player(player_car)
        computer_car.move()

        game_logic.handle_collision(player_car, computer_car, game_info)

        if game_info.game_finished():
            blit_text_center(WIN, MAIN_FONT, "You won the game!")
            pygame.time.wait(5000)
            game_info.reset()
            player_car.reset()
            computer_car.reset()


    pygame.quit()


if __name__ == "__main__":
    main()