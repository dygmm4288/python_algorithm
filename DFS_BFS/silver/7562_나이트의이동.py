import sys
readline = sys.stdin.readline
from queue import deque
# 나이트가 a 지점에서 b지점으로 옮기는데 필요한 최소 횟수

T = int(readline())
for _ in range(T) :
    n = int(readline())
    _map = [[0] * n for _ in range(n)]
    # func
    in_range = lambda y,x : y >= 0 and y < n and x >= 0 and x < n 
    
    # 0 ~ n-1
    y1,x1 = map(int,readline().split())
    y2,x2 = map(int,readline().split())
    
    q = deque([[y1,x1]])
    ret = 0
    while q :
        y,x = q.popleft()
        #찾았으면 답 리턴
        if y == y2 and x == x2 :
            break 
        dy = [-1,-2,-2,-1,1,2,2,1]
        dx = [-2,-1,1,2,2,1,-1,-2]
        
        for i in range(8) :
            ny = dy[i] + y
            nx = dx[i] + x
            if in_range(ny,nx) and _map[ny][nx] == 0 :
                _map[ny][nx] = _map[y][x] + 1
                q.append([ny,nx])
    print(_map[y2][x2])
            
    