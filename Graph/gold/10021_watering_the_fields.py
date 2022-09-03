import sys
readline = sys.stdin.readline
import heapq

n,c = map(int,readline().split())
nodes = []
for _ in range(n):
    nodes.append((tuple(map(int,readline().split()))))

adj = []
for i in range(n) :
    temp = []
    for j in range(n) :
        if i != j :
            temp.append(j)
    adj.append(temp)


def get_cost(a,b) :
    x,y = nodes[a]
    x2,y2 = nodes[b]
    return (x-x2)**2 + (y-y2)**2
def mst(n,c) :
    ret = 0
    min_weight = [sys.maxsize] * (n+1)
    added = [False] * n

    min_weight[0] = 0
    u = -1
    for _ in range(n) :
        flag = False
        _min = sys.maxsize
        for v in range(n) :
            # 트리에 속하지 않은 것 중에 간선이 제일 작은 것을 선택
            # 초기 노드 0 세팅
            if u == -1 :
                u = 0
                flag= True
                break
            if u == v :
                continue
            if not added[v] and min_weight[v] < _min :
                flag = True
                _min = min_weight[v]
                u = v
        if not flag :
            return -1
        added[u] = True
        ret += min_weight[u]

        for v in range(n) :
            cost = get_cost(u,v)
            if not added[v] and min_weight[v] > cost >= c :
                min_weight[v] = cost
    return ret            
        




""" 
# added: 해당 정점이 트리에 포함되어있는지 확인하는 배열
added = [False] * n
# min_weight: 현재 만들어진 트리의 인접한 간선 중 해당 정점에 닿는 최소 간선 정보 저장하는 배열
min_weight = [sys.maxsize] * n

min_weight[0] = 0
ret = 0
count = 0
for u in range(n) :
    # 트리에 추가할 정점 u를 찾는다
    # 현재 이 문제의 경우 모든 노드들에 대한 경로가 존재한다.
    
    if min_weight == sys.maxsize :
        continue
    count += 1
    added[u] = True
    # 트리에 추가된 간선 결과값에 더하기
    ret += min_weight[u]
    # 이 반복문에서 다음 트리에 추가할 적절한 간선을 추가한다
    for v in range(n) :
        cost = get_cost(u,v) 
        # 트리에 포함되지 않았으면서 트리 인접 간선 중 최소 간선을 가진 정점 선택
        if not added[v] and min_weight[v] > cost >= c:
            min_weight[v] = cost
if count == n :
    print(ret)
else :
    print(-1)

def mst(n,c) :
    ret = 0
    min_weight = [sys.maxsize] * n
    added = [False] * n

    min_weight[0] = 0

    for _ in range(n) :
        # 트리에 속한 노드 하나를 선택 해야하나??

        # 트리에서 포함되지 않았으면서 트리 인접 간선 중 최소 간선 찾기
        next_node = [-1,sys.maxsize]
        for v in range(n) :
            # u == v일 경우 그냥 스킵된다
            cost = get_cost(u,v)
            if not added[v] and min_weight[v] > cost >= c :
                # 최소 간선 갱신
                min_weight[v] = cost
                # 조건에 맞는 간선 중 제일 작은 간선을 갖는 노드 선택
                if next_node[1] > min_weight[v] :
                    next_node = [v,min_weight[v]]
        # 노드가 하나도 없을 경우에는 스패닝 트리를 구성할 수 없다
        if next_node[0] == -1 :
            return -1
        # 찾은 노드는 트리에 추가한다
        added[next_node[0]] = True
        # 다음 찾을 노드로 정한다
        
        ret += next_node[1]
    return ret
def mst(n,c) :
    ret = 0
    min_weight = [sys.maxsize] * n
    added = [False] * n

    min_weight[0] = 0
    u = -1
    for _ in range(n) :
        flag = False
        _min = sys.maxsize
        for v in range(n) :
            # 지금 구성된 트리 중에서 가장 작은 간선을 찾는다
            if not added[v] and (u == -1 or min_weight[v] < _min) :
                u =v
                flag = True
    
        if not flag :
            return -1
        ret += min_weight[u]
        added[u] = True
        for v in range(n) :
            cost = get_cost(u,v)
            if not added[v] and min_weight[v] > cost >= c:
                min_weight[v] = cost
        print(u,min_weight)
    return ret    
print(mst(n,c))
'''
