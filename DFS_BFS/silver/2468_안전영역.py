import sys
readline = sys.stdin.readline

n = int(readline())

board = [list(map(int,readline().split())) for _ in range(n)]
def in_range(y,x) :
    return y >=0 and y < n and x >=0 and x < n
def dfs(stack,height,board,visited) :
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    while stack :
        y,x = stack[-1]
        visited[y][x] = True
        flag = False
        for i in range(4) :
            ny = dy[i] + y
            nx = dx[i] + x
            if (in_range(ny,nx) and 
                not visited[ny][nx] and
                board[ny][nx] > height 
               ) :
                stack.append([ny,nx])
                visited[ny][nx] = True
                flag = True
        if not flag :
            stack.pop()
    
ret = 1

for height in range(1,100) :
    visited = [[False] * n for _ in range(n)]
    cand = 0    
    for y in range(n) :
        for x in range(n) :
            if not visited[y][x] and board[y][x] > height:
                dfs([[y,x]],height,board,visited)
                cand += 1
    ret = max(ret,cand)
print(ret)
    