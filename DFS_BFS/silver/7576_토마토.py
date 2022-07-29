import sys
readline = sys.stdin.readline
from queue import deque
m,n = map(int,readline().split())
box = []
cand = []
riper = []
for y in range(n) :
    box.append([])
    riper.append([])
    for x,tomato in enumerate(map(int,readline().split())) :
        if tomato == 1 :
            cand.append([y,x])
        riper[y].append(tomato)
        box[y].append(tomato)

def bfs(cand,box,riper,n,m) :
    q = deque(cand)
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    in_range = lambda y,x : y >= 0 and y < n and x >= 0 and x < m
    ret = 0
    while q :
        top = q.popleft()
        for i in range(4) :
            ny = dy[i] + top[0]
            nx = dx[i] + top[1]
            if (in_range(ny,nx) and
                box[ny][nx] == 0 and
                riper[ny][nx] == 0 
               ) :
                riper[ny][nx] = riper[top[0]][top[1]] + 1
                ret = max(ret,riper[ny][nx])
                q.append([ny,nx])
    return ret

ret = bfs(cand,box,riper,n,m)
def check(riper) :
    for inner in riper :
        if 0 in inner :
            return False
    return True
print(ret-1 if check(riper) else -1)
        
            
         
         
            
         