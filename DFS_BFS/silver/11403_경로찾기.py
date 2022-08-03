import sys
readline = sys.stdin.readline

n = int(readline())
adj = [list(map(int,readline().split())) for _ in range(n)]

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if adj[i][k] and adj[k][j] :
                adj[i][j] = 1
for i in range(n) :
    print(' '.join(map(str,adj[i])))



