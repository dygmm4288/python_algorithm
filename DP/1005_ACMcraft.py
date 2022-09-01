import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10000)
def solution(here,buildings,adj,cache) :
    ret = cache[here]
    if ret != -1 :
        return ret
    # 다음 위치로 갈 곳이 없을 때
    if not adj[here] :
        return buildings[here]
    
    for there in adj[here] :
        ret = max(
            ret,
            solution(there,buildings,adj,cache) + buildings[here]
        )
    cache[here] = ret
    return ret

for _ in range(int(readline())) :
    N,K = map(int,readline().split())
    buildings = [0] + list(map(int,readline().split()))
    
    adj = [[] for _ in range(N+1)]
    for _ in range(K) :
        a,b = map(int,readline().split())
        adj[b].append(a)
    W = int(readline())
    cache = [-1] * (N+1)
    print(solution(W,buildings,adj,cache))