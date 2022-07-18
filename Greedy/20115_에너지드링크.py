import sys
readline = sys.stdin.readline

n = int(readline())
drinks = list(map(int,readline().split()))

drinks.sort(reverse=True)
ret = drinks[0]
for i in range(1,n):
    ret += drinks[i] / 2
print(ret)

