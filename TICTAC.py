#Function to display the board
def print_board(board):
    for row in  board:
        print(" | ".join(row))
        print("-" *9)

#Function to check the winner
def check_winner(board):
    #Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return True

    #Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] !="":
                return True

    #Check diagonals
    if board[0][0] == board[1][1] == board[2][2] !="":
        return True

    if board[0][2] == board[1][1] == board[2][0] !="":
        return True

    return False

#Main Program
board = [["" for _ in range(3)] for _ in range(3)]
player = "X"

for turn in range(9):
    print("\nCurrent Board:")
    print_board(board)

    print(f"Player {player}'s Turn")

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] == "":
        board[row][col] = player

        #Check if current player has won
        if check_winner(board):
            print("\nFinal Board:")
            print_board(board)
            print(f"Player {player} Wins!")
            break

        #Change player
        player = "O" if player == "X" else "X"

    else:
            print("Cell already occupied. Try again.")

else:
        #Execute if all 9 turns are completed without a winner
        print("\nFinal Board:")
        print_board(board)
        print("Game Draw!")
# OUTPUT
# Current Board:

#  |  | 
# ---------

#  |  | 
# ---------

#  |  | 
# ---------
# Player X's Turn
# Enter row (0-2): 0
# Enter column (0-2): 0

# Current Board:
# X |  | 
# ---------

#  |  | 
# ---------

#  |  | 
# ---------
# Player O's Turn
# Enter row (0-2): 1
# Enter column (0-2): 0

# Current Board:
# X |  | 
# ---------
# O |  | 
# ---------

#  |  | 
# ---------
# Player X's Turn
# Enter row (0-2): 0
# Enter column (0-2): 1

# Current Board:
# X | X | 
# ---------
# O |  | 
# ---------

#  |  | 
# ---------
# Player O's Turn
# Enter row (0-2): 1
# Enter column (0-2): 1

# Current Board:
# X | X | 
# ---------
# O | O | 
# ---------

#  |  | 
# ---------
# Player X's Turn
# Enter row (0-2): 0
# Enter column (0-2): 2

# Final Board:
# X | X | X
# ---------
# O | O | 
# ---------

#  |  | 
# ---------
# Player X Wins!
