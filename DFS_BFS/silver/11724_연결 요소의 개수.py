import sys
readline = sys.stdin.readline

n,m = map(int,readline().split())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m) :
    a,b = map(int,readline().split())
    adj[a].append(b)
    adj[b].append(a)
ret = 0
for i in range(1,n+1) :
    if not visited[i] :
        ret += 1
        stack = [i]
        visited[i] = True
        while stack :
            flag = False
            here = stack[-1]
            for there in adj[here] :
                if not visited[there] : 
                    visited[there] = True
                    flag = True
                    stack.append(there)
            if not flag :
                stack.pop()
print(ret)


            

