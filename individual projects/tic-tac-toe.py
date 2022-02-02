'''
Solo Checkpoint 02
Author: Nathan Burnett
'''
NAME_INDEX = 0
SYMBOL_INDEX = 1

def main():
    player_dict = get_players()
    player, turn = player_start(player_dict)
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board, player_dict)
        player, turn = next_player(player, player_dict, turn)
    display_board(board)
    
    if has_winner(board) == True:
        print('(ง ͠ ͠° ل͜ °)ง')
        print(f"Congratulations to {player[NAME_INDEX]}! You have won!")
    elif is_a_draw(board) == True:
        print('(ノಠ益ಠ)ノ彡┻━┻')
        print('sorry, looks like everyone is a loser this time around.')
        replay = input('Do you want to try again?(y or n):')
        if replay == 'y':
            main()
        
        else:
            print('No worries! Good Bye!')
            
     
    
def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    board = []
    for square in range(9):
        board.append(square + 1)

    return board

def display_board(board):
    ''' Displays the current board
        return: None
    '''
    print()
    print(f" {board[0]} |  {board[1]}  | {board[2]}")
    print('---+-----+---')
    print(f" {board[3]} |  {board[4]}  | {board[5]}")
    print('---+-----+---')
    print(f" {board[6]} |  {board[7]}  | {board[8]}")
    print()


def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board, player_dict):
        square = int(input(f"{player[NAME_INDEX]}'s turn to choose a square (1-9): "))
        if board[square-1] == 'x':
            print(f'Sorry, that spot is taken already by {board[square-1]}')
            print('')
            make_move(player,board, player_dict)
        
        elif board[square-1] == 'o':
            print(f'Sorry, that spot is taken already by {board[square-1]}')
            print('')
            make_move(player,board, player_dict)

        else:
            board[square - 1] = player[SYMBOL_INDEX]      

def player_start(player_dict):
    if player_dict['player_one'][SYMBOL_INDEX] == 'x':
        turn = 'one'
        return player_dict['player_one'], turn

    elif player_dict['player_one'][SYMBOL_INDEX] == 'o':
        turn = 'two'
        return player_dict['player_two'], turn

def next_player(player, player_dict, turn):
    if turn == 'one':
       player = player_dict['player_two']
       turn = 'two'
       return player, turn

    elif turn == 'two':
       player = player_dict['player_one']
       turn = 'one'
       return player, turn


def get_players():
    confirmation = 'n'
    while confirmation == 'n':
        player_one_name = input('Player One, what is your name?:')
        player_two_name = input('Player two, what is your name?:')
        player_one_symbol = input(f'Player one who goes by the name of {player_one_name}, please select either "x" or "o": ')
        if player_one_symbol == 'x':
            player_two_symbol = 'o'
        else:
            player_two_symbol = 'x'

        print(f'Fear not! Player Two who goes by the name of {player_two_name}, you have been automatically assigned {player_two_symbol}!')
        player_dict = {'player_one': [player_one_name, player_one_symbol],
                    'player_two': [player_two_name, player_two_symbol]}

        print('')
        print(f'{player_dict["player_one"][NAME_INDEX]} playing as {player_dict["player_one"][SYMBOL_INDEX]}')
        print(f'{player_dict["player_two"][NAME_INDEX]} playing as {player_dict["player_two"][SYMBOL_INDEX]}')
        print('')

        confirmation = input('Is this correct? (y or n): ')
    
    return player_dict

# run main if this has been called from the command line
if __name__ == "__main__":
    main()