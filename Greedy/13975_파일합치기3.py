import sys,heapq
readline = sys.stdin.readline


T = int(readline())
for _ in range(T) :
    n = int(readline())
    files = []
    for file in list(map(int,readline().split())) :
        heapq.heappush(files,file)
    ret = 0
    while len(files) > 1 : 
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        heapq.heappush(files,a+b)
        ret += a+b
    print(ret)


