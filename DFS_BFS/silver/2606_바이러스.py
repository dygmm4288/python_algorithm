import sys
readline = sys.stdin.readline

n = int(readline())
m = int(readline())
edges = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m) :
    _from, _to = map(int,readline().split())
    edges[_from].append(_to)
    edges[_to].append(_from)

from queue import deque
q = deque([1])
visited[1] = True
ret = 0

while q :
    here = q.popleft()
    for there in edges[here] :
        if not visited[there] :
            ret += 1
            visited[there] = True
            q.append(there)
print(ret)
        
            