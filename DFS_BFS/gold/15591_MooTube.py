import sys
readline = sys.stdin.readline
from collections import deque

n,Q = map(int,readline().split())
adj=[[] for _ in range(n+1)]

for _ in range(n-1) :
    a,b,c = map(int,readline().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

def bfs(start,k) :
    q = deque()
    visited = [False] * (n+1)
    visited[start] = True
    q.append((start,sys.maxsize))
    
    ret = 0
    while q :
        here,cur_usado = q.popleft()
        for there,next_usado in adj[here] :
            usado = min(cur_usado,next_usado)
            if usado < k :
                continue
            if not visited[there] :
                visited[there] = True
                q.append((there,usado))
                ret += 1
    return ret
for _ in range(Q) :
    k,v = map(int,readline().split())
    print(bfs(v,k))


            
    