import sys
readline = sys.stdin.readline
from queue import PriorityQueue

n = int(readline())
pq = PriorityQueue()
subjects = [list(map(int,readline().split()[1:])) for _ in range(n)]

subjects.sort(key = lambda x : (x[0],x[1]))

pq.put(-sys.maxsize)

ret = 1
for subject in subjects :
    start,end = subject
    last_time = pq.get()
    
    if last_time > start :
        ret += 1
        pq.put(last_time)
    pq.put(end)
print(ret)

