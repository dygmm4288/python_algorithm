import sys
readline = sys.stdin.readline
from queue import deque

n = int(readline())
paint = []
other_paint = []

for _ in range(n) :
    line = list(map(str,readline().strip()))
    paint.append(line)
    other_paint.append(list(map(lambda x : x if x != 'G' else 'R',line)))

original_visited = [[False]*n for _ in range(n)]
other_visited = [[False] * n for _ in range(n)]

def bfs(y,x,visited,paint,n) :
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    in_range = lambda y,x : y >= 0 and y < n and x >= 0 and x < n
    q = deque()
    q.append([y,x])
    visited[y][x] = True
    while q :
        here = q.popleft()
        for i in range(4) :
            ny = dy[i] + here[0]
            nx = dx[i] + here[1]
            if (in_range(ny,nx) and 
                not visited[ny][nx] and
                paint[ny][nx] == paint[y][x]
               ): 
                visited[ny][nx] = True
                q.append([ny,nx])
origin_ret = 0
other_ret = 0
for y in range(n) :
    for x in range(n) :
        if not original_visited[y][x] :
            origin_ret += 1
            bfs(y,x,original_visited,paint,n)
        if not other_visited[y][x] :
            other_ret += 1
            bfs(y,x,other_visited,other_paint,n)
print(origin_ret, other_ret)