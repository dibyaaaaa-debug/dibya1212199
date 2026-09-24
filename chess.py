#function to print the chessboard
def print_board(board):
    for row in board:
        print(" ".join(row))

#function to check if a queen can be placed safely
def is_safe(board,row,col):
    #check the column
    for i in range(row):
        if board[i][col]=='Q':
            return False
    #check the diagonal
    i,j=row-1,col-1
    while i>=0 and j>=0:
        if board[i][j]=='Q':
            return False
        i-=1
        j-=1
    i,j=row-1,col+1
    while i>=0 and j<8:
        if board[i][j]=='Q':
            return False
        i-=1
        j+=1
    return True
#backtrackung function
def solve(board,row):
    if row==8:
        return True
    for col in range(8):
        if is_safe(board,row,col):
            board[row][col]='Q'
            if solve(board,row+1):
                return True
            board[row][col]='.'
    return False
#main program
board=[['.' for _ in range(8)] for _ in range(8)]
if solve(board,0):
    print_board(board)
else:
    print("No solution exists")