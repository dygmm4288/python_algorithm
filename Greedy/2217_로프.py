import sys
readline = sys.stdin.readline

n = int(readline())
ropes = [int(readline()) for _ in range(n)]

ropes.sort(reverse=True)

ret = 0
for i in range(len(ropes)) :
    ret = max(ret,ropes[i] * (i + 1))
print(ret)