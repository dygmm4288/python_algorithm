import sys
readline = sys.stdin.readline

T = int(readline())

def dfs(y,x,board,visited,n,m) :
    stack = [[y,x]]
    visited[y][x] = True
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    in_range = lambda y,x : y >= 0 and y < n and x >= 0 and x < m
    while stack :
        top = stack[-1]
        flag = False
        for i in range(4) :
            ny = dy[i] + top[0]
            nx = dx[i] + top[1]
            if (in_range(ny,nx) and
                board[ny][nx] == 1 and
                not visited[ny][nx]
               ) :
                stack.append([ny,nx])
                visited[ny][nx] = True
                flag = True
        if not flag :
            stack.pop()
    return None

for _ in range(T) :
    n,m,k = map(int,readline().split())
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    # position of cabbage
    for _ in range(k) :
        y,x = map(int,readline().split())
        board[y][x] = 1
    ret = 0
    for y in range(n) :
        for x in range(m) :
            if board[y][x] == 1 and not visited[y][x] :
                ret += 1
                dfs(y,x,board,visited,n,m)
    print(ret)