import sys
readline = sys.stdin.readline
from queue import deque

m,n,h = map(int,readline().split())
tomato = []

q = deque()
for z in range(h) :
    temp = []
    for y in range(n) :
        temp.append(list(map(int,readline().split())))
        for x in range(m) :
            if temp[y][x] == 1 :
                q.append([z,y,x])
    tomato.append(temp)
in_range = lambda z,y,x : (z >= 0 and z < h and 
                           y >= 0 and y < n and
                           x >= 0 and x < m 
                          )
ret = 1
while q :
    z,y,x = q.popleft()
  
    dz = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dx = [0,0,0,0,-1,1]
    
    for i in range(6) :
        nz = z + dz[i] 
        ny = y + dy[i] 
        nx = x + dx[i]
        if (in_range(nz,ny,nx) and
            tomato[nz][ny][nx] == 0
           ) :
            tomato[nz][ny][nx] = tomato[z][y][x] + 1
            ret = max(ret,tomato[nz][ny][nx])
            q.append([nz,ny,nx])
    
    
def check(tomato) :
    for z in range(h) :
        for y in range(n) :
            for x in range(m) :
                if tomato[z][y][x] == 0 :
                    return False
    return True
print(ret-1 if check(tomato) else -1)
        
        