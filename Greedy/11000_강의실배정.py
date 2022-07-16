import sys
readline = sys.stdin.readline
from queue import PriorityQueue

n = int(readline())
subjects = []
pq = PriorityQueue()
for _ in range(n) :
    subjects.append(list(map(int,readline().split())))
# first condition : S(start time)
# second condition : T(end time)
# S[i], T[i] <= S[j] , T[j] (if, i<j)
subjects.sort(key = lambda x : (x[0],x[1]))

# initial data
pq.put(-1)
ret = 1

for subject in subjects :
    [start,end] = subject
    last_time = pq.get()
    # it cant be in the same class, so increase 
    if last_time > start :
        ret += 1
        # last_time means that earlist finish class time
        pq.put(last_time)
    pq.put(end)
print(ret)