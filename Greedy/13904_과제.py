import sys
readline = sys.stdin.readline
from queue import PriorityQueue
# 하루에 한 개 과제
# 과제마다 마감일이 있다.
# 과제마다 얻을 수 있는 점수가 있다
# 가장 점수를 많이 받을 수 있도록

n = int(readline())
tasks = [[] for _ in range(1001)]

for i in range(n) :
    d,w = map(int,readline().split())
    if not tasks[d] :
        tasks[d] = []
    tasks[d].append(w)

pq = PriorityQueue()

ret = 0
for i in range(1000,0,-1) :
    for d in tasks[i] :
        pq.put(-d)
    if not pq.empty() :
        value = pq.get()
        ret += value
print(-ret)
 


