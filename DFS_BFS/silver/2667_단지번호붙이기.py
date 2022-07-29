import sys
readline = sys.stdin.readline
from queue import deque

n = int(readline())
board = [readline().strip() for _ in range(n)]
visited = [[False]*n for _ in range(n)]
ret = []

def bfs(y,x,board,visited,n) : 
    visited[y][x] = True
    q = deque([[y,x]])
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    in_range = lambda y,x : y >= 0 and y < n and x >= 0 and x < n
    ret = 1
    while q :
        here = q.popleft()
        for i in range(4) :
            ny = here[0] + dy[i]
            nx = here[1] + dx[i]
            if (in_range(ny,nx) and 
                board[ny][nx] == '1' and
                not visited[ny][nx]
               ) :
                q.append([ny,nx])
                visited[ny][nx] = True
                ret += 1
    return ret            
            
#solution
for y in range(n) :
    for x in range(n) :
        if not visited[y][x] and board[y][x] == '1' :
            ret.append(bfs(y,x,board,visited,n))
ret.sort()
print(len(ret))
for r in ret :
    print(r)
                
            

