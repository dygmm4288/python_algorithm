import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**6)

m,n,k = map(int,readline().split())
board = [[0] * n for _ in range(m)]
for _ in range(k) :
    x,y,x2,y2 = map(int,readline().split())
    for i in range(y,y2) :
        for j in range(x,x2) :
            board[i][j] = 1
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def dfs(y,x) :
    count = 1
    board[y][x] = 1
    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x
        if 0<=ny<m and 0<=nx<n and board[ny][nx] == 0 :
            count += dfs(ny,nx) 
    return count
ret = []
for y in range(m) :
    for x in range(n) :
        if board[y][x] == 0 :
            ret.append(dfs(y,x))
print(len(ret))
print(' '.join(map(str,sorted(ret))))