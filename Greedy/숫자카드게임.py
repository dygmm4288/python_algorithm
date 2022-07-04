n, m = map(int,input().split())
best = -1
    for i in range(n):
    data = list(map(int,input().split()))
    best = max(best, min(data))
print(best)