game_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def display_game(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def choose_player(player1, player2):
    player1 = input("which one you choose? X or O ").upper()
    while player1 not in ["X", "O"]:
        print("Invalid input. please choose either 'X' or 'O'. ")
        player1 = input("which one you choose? X or O ").upper()
    
    player2 = "O" if player1 == "X" else "X"
    current_player = player1

    print(f"player 1 is '{player1}' and player 2 is '{player2}' ")
    return player1, player2, current_player 


def player_move(board, current_player):
    valid = False
    while not valid:
        try:
            move = int(input(current_player + "'s turn. choose a position (1-9):"))
            if move >=1 and move<=9:
                index = move - 1 
                if board[index] == "-":
                    board[index] = current_player
                    valid = True
                else:
                    print("This position is already taken. try again.")
            else:
                print("invalid number. choose between 1 and 9 ")
        except ValueError:
            print("invalid input. please enter a number.")

def check_winner(board):
    if board[0]==board[1]==board[2] != "-":
        return board[0]
    elif board[3]==board[4]==board[5] != "-":
        return board[3]
    elif board[6]==board[7]==board[8] != "-":
        return board[6]
    elif board[0]==board[3]==board[6] != "-":
        return board[0]
    elif board[1]==board[4]==board[7] != "-":
        return board[1]
    elif board[2]==board[5]==board[8] != "-":
        return board[2]
    elif board[0]==board[4]==board[8] != "-":
        return board[0]
    elif board[2]==board[4]==board[6] != "-":
        return board[2]
    elif "-" not in board:
        return "Tie"
    else:
        return None
    
def switch_player(current_player):
    return "O" if current_player == "X" else "X"

def play_game():
    print("welcome to Tic Tac Toe")
    board = ["-"] * 9
    display_game(board)
    player1, player2, current_player =choose_player("", "")
    winner = None

    while winner is None: 
        player_move(board, current_player)
        display_game(board)
        winner = check_winner(board)
        if winner is None:
            current_player = switch_player(current_player)
    
    if winner == "Tie":
        print("It's a tie")
    else:
        print(f"player {winner} wins!")

play_game()