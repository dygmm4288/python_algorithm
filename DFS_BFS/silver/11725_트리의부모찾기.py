import sys
readline = sys.stdin.readline

n = int(readline())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent = [0] * (n+1)

# edges
for _ in range(n-1) :
    a,b = map(int,readline().split())
    adj[a].append(b)
    adj[b].append(a)

stack = [1]
visited[1] = True
while stack : 
    here = stack[-1]
    flag = False
    for there in adj[here] :
        if not visited[there] :
            stack.append(there) 
            visited[there] = True
            parent[there] = here
            flag = True
    if not flag : 
        stack.pop()

for i in range(2,n+1) :
    print(parent[i])
