import sys,collections
readline = sys.stdin.readline

n = int(readline())
x,y = map(int,readline().split())
m = int(readline())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b = map(int,readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,start,end,n) :
    dist = [-1] * (n+1)
    q = collections.deque()
    q.append(start)
    dist[start] = 0
    
    while q :
        me = q.popleft()
        
        for there in graph[me] :
            if dist[there] == -1:
                q.append(there)
                dist[there] = dist[me] + 1
    return dist[end]

ret = bfs(graph,x,y,n)
print(ret)

