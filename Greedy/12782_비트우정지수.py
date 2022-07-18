import sys
readline = sys.stdin.readline

T = int(readline())
for _ in range(T) :
    n,m = map(str,readline().split())
    diff = [0,0]
    for k in range(len(n)):
        if n[k] != m[k] :
            diff[int(n[k])] +=1
    print(min(diff) + abs(diff[0] - diff[1]))