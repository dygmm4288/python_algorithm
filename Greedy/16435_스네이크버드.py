import sys
readline = sys.stdin.readline

N, L = map(int,readline().split())
heights = list(map(int,readline().split()))

heights.sort()
ret = L
for i in range(N):
    if heights[i] > (L + i):
       ret = L + i
       break
    ret = L + i + 1
print(ret)