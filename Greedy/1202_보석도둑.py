# 이전 풀이
'''import sys
stdin = sys.stdin.readline
from queue import PriorityQueue

N, K = map(int,stdin().split())
# gems[0] = weight, gems[1] = Value
gems = []
c = []
pq = PriorityQueue();
# input data
for _ in range(N):
    gems.append(list(map(int,stdin().split())))

for _ in range(K):
    c.append(int(stdin()))

print(gems,c)
# sorted by gems weight
gems.sort(key = lambda x: x[0])
# sorted by bags weight
c.sort()

ret = 0
idx = 0
for bag_weight in c:
    while idx < N and gems[idx][0] <= bag_weight:
        pq.put(-gems[idx][1])
        idx += 1
    if(not pq.empty()) :
      ret += -(pq.get())
print(ret)     
'''

import sys
readline = sys.stdin.readline
from queue import PriorityQueue

n,k = map(int,readline().split())
gems = [list(map(int,readline().split())) for _ in range(n)]
bags = [int(readline()) for _ in range(k)]

pq = PriorityQueue()

# sort in ascending order based on weight of gems and weight of bags
gems.sort(key=lambda x : x[0]) 
bags.sort()

ret = 0
idx =0

for weight in bags :
    while idx < n :
        # put gems in current bags, if the weight of gem can put 
        if gems[idx][0] <= weight :
            pq.put(-gems[idx][1]) 
        else :
            break
        idx += 1  
    # take out the heaviest one, if pq is not empty
    if not pq.empty() ;
        ret += -pq.get()
print(ret)