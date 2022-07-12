board = input()
if board.count('X') % 2 != 0 : print(-1)
else :
    board = board.replace('XXXX','AAAA')
    board = board.replace('XX','BB')
    if board.count('X') > 0 : print(-1)
    else : print(board)