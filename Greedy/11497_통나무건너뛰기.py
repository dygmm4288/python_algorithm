import sys
readline = sys.stdin.readline

T = int(readline())

for _ in range(T) :
    N = int(readline())
    logs = list(map(int,readline().split()))
    logs.sort(reverse=True)
    ret = max(abs(logs[0]-logs[1]),abs(logs[0] - logs[2]))
    for i in range(1,N-2):
        ret = max(ret,abs(logs[i]-logs[i+2]))
    ret = max(ret,abs(logs[-1]-logs[-2]))
    print(ret)