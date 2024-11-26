
def print_board(board):
    print("----------")
    for row in board:
        print(f"| {' | '.join(row)} |")
        print("----------")

def make_move(board,player):
    while True:
        try:
            row,col=map(int,input(f"player: {player} Select the Move between (0,2):  ").split())
            if row not in range(3) and col not in range(3):
                print("Invalid Move.Please Choose a Valid Move")
            elif board[row][col]!='':
                print("This position is already occupied!")
            else:
                board[row][col]=player
                break
        except ValueError:
            print("Move must be in range (0 , 2")

def check_win(board,player):
    for i in range(3):
        if all([cell==player for cell in board[i]]) or all([board[j][i]==player for  j in range(3)]):
            return True
    if board[0][0]==player and  board[1][1]==player and  board[2][2]==player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False
def check_draw(board,player):
    for i in range(3):
        for j in range(3):
            if board[i][j]=='':
                return False
    return True
def tic_tac_toe():
    board=[['' for _ in range(3)] for _ in range(3)]
    players=['X','O']
    player=0
    moves=[['0','0'],['0','1'],['0','2'],['1','0'],['1','1'],['1','2'],['2','0'],['2','1'],['2','2']]
    for move in moves:
        print(f"Move:{'-'.join(move)}")
        print("-----")
    print("---------Board ........")    
    while True:
        print_board(board)
        make_move(board,players[player])
        if check_win(board,players[player]):
            print(f'player: {players[player]} win the Game..\U0001F60A')
            break
        elif check_draw(board,players[player]):
            print('It is a Draw..\U0001F622')
            break
        player=(player+1)%2
tic_tac_toe()
