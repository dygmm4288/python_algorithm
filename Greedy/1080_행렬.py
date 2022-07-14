import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())

board = []
for _ in range(N):
    board.append(list(map(int,readline().strip())))
next_state = []
for _ in range(N) :
    next_state.append(list(map(int,readline().strip())))

ret = -1
# can turn
if N >= 3 and M >= 3 :
    for i in range(N-2):
        for j in range(M-2) :
            if board[i][j] != next_state[i][j]:
                for r in range(i,i+3) :
                    for c in range(j,j+3):
                        board[r][c] = (board[r][c] + 1) % 2
                ret += 1
    # ret start to -1 
    if board == next_state :
        ret += 1
    # not same, so ret = -1
    else : ret = -1
# can't turn
else :
    # same
    if board == next_state :
        ret = 0
print(ret)
    
            