#Chess Project
from BoardSize import board_dim
from printing_chess import print_board
from BoardSize import W, B


def init_board():
    
    board = [["_" for j in range(board_dim)] for i in range(board_dim)]
    
    for i in range(board_dim):
        board[1][i] = "P"
        board[6][i] = "p"
    board[0] = W
    board[7] = B 

    return board


def move_from():
    
    print("Welcome to my python chess program!")
    
    player_turn = "White"
    
    print(f"It is {player_turn}\'s move initially.")
    
    board = init_board()
    
    while True:
        
        print_board(board)
        
        old_square = input("What square is the piece you would like to move on? ")
        old_square = old_square.upper()
        old_row = int(old_square[1]) - 1
        old_column = ord(old_square[0]) - 65
        
        new_square = input("What square would you like to move this piece to? ")
        new_square = new_square.upper()
        new_row = int(new_square[1]) - 1
        new_column = ord(new_square[0]) - 65 
        
        if len(new_square) == 2 or len(old_square) == 2:
            board[new_row][new_column] = board[old_row][old_column]
            board[old_row][old_column] = "_"
            if player_turn == "White":
                player_turn = "Black"
                print(f"It is now {player_turn}\'s turn")
            else:
                player_turn = "White"
                print(f"It is now {player_turn}\'s turn")
                
        else:
            print("You did not enter a valid square on the chess board. Please try again")
            
def rules():
    
        
        
        
            

