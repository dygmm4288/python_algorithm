import sys
readline = sys.stdin.readline

n = int(readline())
ret = '*'
for i in range(n):
    print(ret)
    ret += '*'