import sys
readline = sys.stdin.readline
while True :
    a,b = map(int,readline().split())
    if a == 0 or b == 0 : 
        break
    print(a+b)
    