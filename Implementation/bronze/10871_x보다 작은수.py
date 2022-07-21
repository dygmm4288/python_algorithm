import sys
readline = sys.stdin.readline

n,x = map(int,readline().split())
a = list(map(int,readline().split()))
for value in a :
    if value < x :
        print(value, end=' ')