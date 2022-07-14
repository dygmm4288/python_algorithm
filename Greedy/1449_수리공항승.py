N, L = map(int,input().split())

leakes = list(map(int,input().split()))

leakes.sort()
visited = [False] * N

# 왼쪽부터 막아가는데 최대 길이 L만큼 막아간다
ret = 0
for i in range(N):
    leak = leakes[i]
    cand = [i]
    if visited[i] :
        continue
    if not visited[i] :
        ret += 1
    for j in range(i,N):
        next_leak = leakes[j]
        if (not visited[j] 
            and next_leak - leak + 1 <= L
        ):
            cand.append(j)
    for index in cand:
        visited[index] = True
print(ret)