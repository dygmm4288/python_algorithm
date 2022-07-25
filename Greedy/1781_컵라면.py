import sys
readline = sys.stdin.readline
from queue import PriorityQueue

n = int(readline())
problems = [list(map(int,readline().split())) for _ in range(n)]
deadlines = [[] for _ in range(n+1)]
pq = PriorityQueue()

for [deadline,cup] in problems :
    deadlines[deadline].append(cup)
ret = 0
for i in range(n,0,-1) :
    for j in deadlines[i] :
        pq.put(-j)
    if not pq.empty() :
        ret += pq.get()
print(-ret)