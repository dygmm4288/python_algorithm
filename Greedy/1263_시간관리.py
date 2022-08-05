import sys
readline = sys.stdin.readline

n = int(readline())
times = [tuple(map(int,readline().split())) for _ in range(n)]

times.sort(key=lambda x : -x[1])

last_time = times[0][1] - times[0][0]
for i in range(1,n) :
    t,s = times[i]
    if s > last_time :
        last_time = s - (t + s - last_time)
    else :
        last_time = s - t
if last_time < 0 :
    print(-1)
else : print(last_time)


        
        



