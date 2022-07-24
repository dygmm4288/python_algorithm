import sys
readline = sys.stdin.readline

n,m = map(int,readline().split())
road = [readline().strip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

in_range = (lambda n,m : 
            lambda y,x : y >= 0 and y < n and x >=0 and x < m
           )(n,m)

def dfs(y,x,visited,road) :
    if not in_range(y,x) : return False
    if road[y][x] == 'x' or visited[y][x] == 1 :
        return False
    visited[y][x] = True
    if x  == (m -1) : return True

    dy = [-1,0,1]
    ret = False;
    for i in range(3) :
        ny = dy[i] + y
        nx = 1 + x
        ret = ret or dfs(ny,nx,visited,road)
    return ret

ret = 0
for y in range(n) :
  if dfs(y,0,visited,road) : ret += 1

print(ret)
    
      