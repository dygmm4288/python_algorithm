import sys
readline = sys.stdin.readline

N = int(readline())
s = list(map(int,readline().split()))

s.sort()
ret = 987654321
all = N * 2
for i in  range(N):
    ret  = min(ret, s[i] + s[all-i-1])
print(ret)