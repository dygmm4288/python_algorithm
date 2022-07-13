import sys
readline = sys.stdin.readline
from queue import PriorityQueue

N = int(readline())
dasom = 0
pq = PriorityQueue()
for i in range(N):
    if i == 0 : dasom = int(readline())
    else :
        cand = int(readline())
        pq.put(-cand)
ret = 0
while not pq.empty() :
    cand = pq.get()
    if dasom <= -cand :
        dasom += 1
        pq.put(cand+1)
        ret += 1
print(ret)