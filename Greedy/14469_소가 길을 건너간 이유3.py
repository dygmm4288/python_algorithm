import sys
readline = sys.stdin.readline
from queue import PriorityQueue

N = int(readline())

cows = [0] * N
pq = PriorityQueue()

for i in range(N):
    cows[i] = list(map(int,readline().split()))
    
cows.sort(key=lambda x : x[0])

idx = 0
cur_time = 0

while idx < N or not pq.empty() :
    # 현재 시간(cur_time)안에 소가 도착을 완료했다면 큐에 소를 넣는다
    while idx < N and cur_time >= cows[idx][0] :
        pq.put(cows[idx][1])
        idx += 1
    # 현재 시간안에 소가 있다면 현재 시간 기준 + 소 검문 시간
    if not pq.empty() :
        cur_time += pq.get()
    # 현재 시간안에 소가 없다면 
    elif pq.empty() :
         cur_time = cows[idx][0]
print(cur_time)  
    
    