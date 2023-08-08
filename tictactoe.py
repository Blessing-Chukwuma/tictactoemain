board = []

for i in range(1,11,1):

    board.append(' ')


def display_board(board):


    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    print('-----------')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('-----------')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def receive_input():

    marker = ''

    while marker != 'X' and marker != 'O':

        marker = input("Please input your marker X or O: ").upper()

    return ('X','O') if marker == 'X' else ('O','X')

def player_position(player, position):

     board[position] = player

def win_check(board):

    return(

    (board[1] == board[2] == board[3]) and (board[1] != ' ' and (board[2] !=' ' and board[3] != ' ')) or 

    (board[4] == board[5] == board[6]) and (board[4] != ' ' and (board[5] != ' ' and board[6] != ' ')) or

    (board[7] == board[8] == board[9]) and (board[7] != ' ' and (board[8] != ' ' and board[9] != ' ')) or

    (board[1] == board[5] == board[9]) and (board[1] != ' ' and (board[5] != ' ' and board[9] != ' ')) or

    (board[7] == board[5] == board[3]) and (board[7] != ' ' and (board[5] != ' ' and board[3] != ' ')) or

    (board[1] == board[4] == board[7]) and (board[1] != ' ' and (board[4] != ' ' and board[7] != ' ')) or

    (board[2] == board[5] == board[8]) and (board[2] != ' ' and (board[5] != ' ' and board[8] != ' ')) or

    board[3] == board[6] == board[9] and (board[3] != ' ' and (board[6] != ' ' and board[9] != ' '))

    )

def start_game():
    while True:
        response = input('Do you want to start the game? Y or N: ').upper()

        if response == 'Y':
            return True
        elif response == 'N':
            print("Thanks for playing")
            # return False
            exit()
        else:
            print("Please input 'Y' or 'N' ")

def board_full(board):

    for i in range(1,10,1):

        if board[i] == ' ': 
            return False   

    else:
        return True


def tictactoe():

    start_game()

    player1,player2 = receive_input()

    current_player = player1

    #current_board = board1

    while True:

        display_board(board)

        position = int(input(f"Player {current_player}, Choose position 1 - 9: "))

        if position < 10 and position >= 1:
           
            if board[position] == ' ':

                player_position(current_player,position)

                if win_check(board):

                    display_board(board)

                    print(f"{current_player} wins!")

                    break


                if board_full(board):

                    display_board(board)
                    print('Its a draw')

                    break

                current_player=player2 if current_player==player1 else player1

            else: 

                print('Slot is Taken!')

                continue
            
        else:
            position = int(input(f"Player {current_player}, Choose position 1 - 9 ,"))
            
tictactoe()
