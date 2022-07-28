import sys

readline = sys.stdin.readline

n, m, v = map(int, readline().split())
from collections import defaultdict
edges = defaultdict(list)

for _ in range(m):
    _from, _to = map(int, readline().split())
    edges[_from].append(_to)
    edges[_to].append(_from)
for edge in edges:
    edges[edge].sort()
  

def dfs(here, visited, edges,ret):
    visited[here] = True
    ret.append(here)
    for _next in edges[here]:
        if not visited[_next]:
            dfs(_next, visited, edges,ret)


def bfs(start, visited, edges):
    from queue import deque
    q = deque([start])
    visited[start] = True
    ret = []
    while len(q):
        here = q.popleft()
        ret.append(here)
        for _next in edges[here]:
            if not visited[_next]:
                q.append(_next)
                visited[_next] = True
    print(' '.join(map(str,ret)))

visited = [False] * (n + 1)
ret = []
dfs(v, visited, edges,ret)
print(' '.join(map(str,ret)))
visited = [False] * (n + 1)
bfs(v, visited, edges)
