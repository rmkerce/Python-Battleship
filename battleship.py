#-----------------------Welcome to Battleship!-----------------------
#This program will be an enhanced version of the CodeAcademy version
#of the famous 2 player game. Ships will be added, and a full computer AI will randomly guess coordinates.  

from random import randint

board = []                        #Initialize the list

for x in range(20):
    board.append(["O"] * 20)

space = " "
def print_board(board):
    for row in board:
        print (space.join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

carrier_row = random_row(board)      #Set the computer ships on the board
carrier_col = random_col(board)

cruiser_row = random_row(board)
cruiser_col = random_col(board)

destroyer_row = random_row(board)
destroyer_col = random_col(board)

battleship_row = random_row(board)
battleship_col = random_col(board)

lcs_row = random_row(board)
lcs_col = random_col(board)

# Playing a game
for turn in range(10):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))


    if (guess_row == carrier_row and guess_col == carrier_col) or (guess_row == cruiser_row and guess_col == cruiser_col) or (guess_row == destroyer_row and guess_col == destroyer_col) or (guess_row == battleship_row and guess_col == battleship_col) or (guess_row == lcs_row and guess_col == lcs_col):
        print ("Congratulations! You sunk my ",ship_name,"!")
        break
    else:
        if turn == 9:
            print ("Game Over")
        elif (guess_row < 0 or guess_row > 20) or (guess_col < 0 or guess_col > 20):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    # Print the turn for the user!
    print ("End of turn",(turn + 1),"\n")
    print_board(board)
