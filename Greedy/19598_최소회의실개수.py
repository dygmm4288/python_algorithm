import sys
readline = sys.stdin.readline
from queue import PriorityQueue

n = int(readline())
meetings = [list(map(int,readline().split())) for _ in range(n)]
meetings.sort(key=lambda x : (x[0],x[1]))

q = PriorityQueue()
q.put(meetings[0][1])

ret = 1
for i in range(1, n):
    if not q.empty() :
        last_time = q.get()
        if last_time > meetings[i][0] :
            ret += 1
            q.put(last_time)
        q.put(meetings[i][1])    
print(ret)
    

