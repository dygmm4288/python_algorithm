import sys
readline = sys.stdin.readline

n,m = map(int,readline().split())
board = [readline().strip() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
from queue import deque
q = deque([[0,0]])
visited[0][0] = 1

dy = [1,-1,0,0]
dx = [0,0,1,-1]
in_range = lambda y,x : (y >= 0 and 
                         y < n and 
                         x >= 0 and
                         x < m)
while q :
    y,x = q.popleft()
  
    for i in range(4) :
        ny,nx = dy[i] + y, dx[i] + x
      
        if (in_range(ny,nx) and
            visited[ny][nx] == 0 and
            board[ny][nx] == '1'
           ) :
             q.append([ny,nx])
             visited[ny][nx] = visited[y][x] + 1
print(visited[n-1][m-1])