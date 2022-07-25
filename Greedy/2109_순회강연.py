import sys
readline = sys.stdin.readline
from queue import PriorityQueue

n = int(readline())
lecture = [[] for _ in range(10001)]

for _ in range(n):
    p,d = map(int,readline().split())
    lecture[d].append(p)
pq = PriorityQueue()
ret = 0
for i in range(10000,0,-1) :
    for p in lecture[i] :
        pq.put(-p)
    if not pq.empty() :
        
        ret += pq.get()
print(-ret)


