import sys
readline = sys.stdin.readline
from collections import deque

T = int(readline())
for _ in range(T) :
    n,m = map(int,readline().split())
    jobs = list(map(int,readline().split()))
    q = deque()
    
    for i in range(len(jobs)) :
        q.append([jobs[i],i])
    jobs.sort(reverse=True)
    
    count = 0
    while True :
        cur_job = q.popleft()
        if cur_job[0] < jobs[count] :
            q.append(cur_job)
        else :
            count += 1
            if cur_job[1] == m :
                print(count)
                break
    

    