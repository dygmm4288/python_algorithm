import sys
readline = sys.stdin.readline

n = int(readline())
li = list(map(int,readline().split()))
print(min(li),max(li))