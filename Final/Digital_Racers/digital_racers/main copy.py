import pygame
from constants import *
from game.actors.game_info import GameInfo
from game.actors.player import Player
from game.actors.computer_player import Computer_Player
from game.script.game_logic import Game_logic
from game.script.game_settings import Game_Settings



# ----------------------------------------------------------------------------------------------
# __Main__
# ----------------------------------------------------------------------------------------------

def main():
    game_settings = Game_Settings()

    # Settings and Start Menu
    print()
    print('Announcer: Hello! Welcome to our state of the art video ga...')
    input("(press enter to continue)")
    print("Announcer: I am sorry player! Give me one moment while I figure something out. ")
    input("(press enter to continue)")
    print("***steps walking away***  ***Phone Ringing***")
    input("(press enter to continue)")
    print("Announcer (in distance): What do you mean we didnt have enough budget for a GUI main menu?!")
    input("(press enter to continue)")
    print("***Unrecognizable conversation*** ***steps walking back***")
    input("(press enter to continue)")
    print("Well, it seems that there wasnt enough budget for a GUI menu. Regardless, welcome to Digital Racers!")
    
    print("What game mode would you like to play?")
    print("1: Player v Player")
    print("2: Player v Computer")
    game_mode = input("Select your option: ")

    game_settings.set_game_mode(game_mode)

    print()
    print("Before we get to customization of your car.")
    print("What level would you like to play?")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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