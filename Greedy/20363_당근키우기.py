import sys
readline = sys.stdin.readline

x,y = map(int,readline().split())
print(min(x+y+y//10,x+y+x//10))