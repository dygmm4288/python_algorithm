def dfs(here,visited):
  dy = [-1,1,0,0]
  dx = [0,0,-1,1]
  n ,m = len(visited), len(visited[0])
  (y,x) = here
  visited[y][x] = True
  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if ny >= 0 and ny < n and nx >= 0 and nx < m:
      if not visited[ny][nx]:
        dfs((ny,nx),visited)

visited = [
  [False,False,True,True,False],
  [False,False,False,True,True],
  [True,True,True,True,True],
  [False,False,False,False,False]
]

n,m = len(visited), len(visited[0])
cnt = 0
for y in range(n):
  for x in range(m):
    if not visited[y][x]:
      dfs((y,x),visited)
      cnt += 1
print(cnt)


# N, M을 공백으로 구분하여 입력받기
n, m = map(int,input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

def dfs(x,y):
  if x<= -1 or x >= n or y <= -1 or y >= m:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x, y+1)
    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j,) == True:
      result += 1
print(result)

