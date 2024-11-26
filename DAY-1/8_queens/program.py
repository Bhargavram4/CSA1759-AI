

def is_safe(board,row,col):
    for i in range(row):
        if board[i]==col:
            return False
        if board[i]-i==col-row:
            return False
        if board[i]+i==col+row:
            return False
    return True
def solve(board,row):
    if row==len(board):
        return True

    for col in range(len(board)):
        if is_safe(board,row,col):
            board[row]=col
            if solve(board,row+1):
                return True
        board[row]=-1
def ans_board(board):
    for i in range(len(board)):
        row=['\u2655' if col==board[i] else '.' for col in range(len(board))]
        print(''.join(row))
    print()
            
def solve_8_queens():
    # initialize chessboard rows
    board=[-1]*8

    #solve the queens using backtracking

    if solve(board,0):
        ans_board(board)
    else:
        print('Solution Not Found')



solve_8_queens()
