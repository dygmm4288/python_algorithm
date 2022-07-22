import sys
readline = sys.stdin.readline

a,b,c = map(int,readline().split())
li = [a,b,c]
li.sort()
print(li[-2])

