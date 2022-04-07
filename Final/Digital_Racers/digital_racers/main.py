from constants import *
from game.actors.game_info import GameInfo
from game.actors.player import Player
from game.actors.computer_player import Computer_Player
from game.script.game_logic import Game_logic
from assets.levels.level_abstract import Level_Abstract
from assets.levels.race_track_level import Race_Track_Level
from assets.levels.water_way_level import Water_Way_Level
import random
from game.directing.director import Director

# ----------------------------------------------------------------------------------------------
# __Main__
# ----------------------------------------------------------------------------------------------

def main():

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
    
    #Game Mode Selection
    print("What game mode would you like to play?")
    print()
    print("1: Player v Player")
    print("2: Player v Computer")
    print()
    game_mode = int(input("Select your option: "))


    #Level Selection
    print()
    print("Before we get to customization of your car.")
    print("What level would you like to play?")
    print()

    for map in range(len(level_list)):
        print(level_list[map])

    print()

    level_selection = int(input("Please Select Option by inputing number: "))

    if level_selection == 1:
        level = Race_Track_Level()
        level.set_level_properties(game_mode)
        level.set_player_types()
        print("You have selected Race Track Speed Way!")
        print(f"Lets select your Race {level.get_vehicle_type()} color!")
        print("Here are your options: ")
    
    elif level_selection == 2:
        level = Water_Way_Level()
        level.set_level_properties(game_mode)
        level.set_player_types()
        print(f"Lets select your Race {level.get_vehicle_type()} color!")
        print("Here are your options: ")
        print()
        print()



    #Vehical Selection and player(s) instance creation
    list = level.get_vehicle_list()

    #vehical selection for player v player
    if game_mode == 1:
        for color in range(len(list)):
            print(list[color])

        choice = input('Player 1, Which one do you want (type color): ')
        vehicle = level.select_vehicle(choice)
        Player_One = Player(MAX_VEL, MAX_ROTATION)
        Player_One.set_player_name('Player_One')
        Player_One.set_vehicle(vehicle)
        Player_One.set_control_type(level.get_player_one_type())
        Player_One.set_start_pos(level.player_1_start_pos)
        list.remove(choice)

        print()
        print('Player 2, its your turn! Here are your options: ')
        print()

        for color in range(len(list)):
                print(list[color])
        
        print()

        choice = input('Player 2, Which one do you want (type color): ')
        vehicle = level.select_vehicle(choice)
        Player_Two = Player(MAX_VEL, MAX_ROTATION)
        Player_Two.set_player_name('Player_Two')
        Player_Two.set_start_pos(level.player_2_start_pos)
        Player_Two.set_control_type(level.get_player_two_type())
        Player_Two.set_vehicle(vehicle)

        print()

    #vehical selection for player vs bot
    elif game_mode == 2:
        for color in range(len(list)):
            print(list[color])

        print()
        choice = input('Player 1, Which one do you want (type color): ')
        vehicle = level.select_vehicle(choice)
        Player_One = Player(MAX_VEL, MAX_ROTATION)
        Player_One.set_player_name('Player_One')
        Player_One.set_start_pos(level.player_1_start_pos)
        Player_One.set_vehicle(vehicle)
        Player_One.set_control_type(level.get_player_one_type())
        list.remove(choice)

        print()
        print('The Computer it choosing its Color!')
        print()

        choice = random.choice(list)
        print(f"The computer chose {choice}!")
        vehicle = level.select_vehicle(choice)
        Player_Two = Computer_Player(START_VEL_BOT, START_ROTATION_BOT)
        Player_Two.set_path(level.get_bot_path())
        Player_Two.set_player_name('Player_Two')
        Player_Two.set_start_pos(level.player_2_start_pos)
        Player_Two.set_control_type(level.get_player_two_type())
        Player_Two.set_vehicle(vehicle)

    print("The game is all ready to go. Please go to the pygame screen!")


    #compile of images for map
    ground = level.get_ground()
    track = level.get_track()
    finish = level.get_finish()
    finish_pos = level.get_finish_position()
    track_border = level.get_track_border()


    Images = [(ground, (0, 0)), (track, (0, 0)),
          (finish, finish_pos), (track_border, (0, 0))]


    director = Director(Player_One, Player_Two, level, Images)
    director.start_game()
    
main()