#DFS 메서드 정의
def dfs(graph,v,visited):
    visited[v] = True
    print(v, end=' ')
    for next in graph[v]:
        if not visited[next]:
            dfs(graph,next,visited)
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

dfs(graph,1,visited)

#큐(Queue)사용을 위한 라이브러리 import
from collections import deque
#BFS메서드 정의
def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        here = queue.popleft()
        print(here, end=' ')
        for next in graph[here]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

visited = [False] * 9
print(' ')
bfs(graph,1,visited)