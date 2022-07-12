import sys
stdin = sys.stdin.readline
while True :
    try :
        a, b, c = map(int,stdin().split())
        print(max(abs(a-b), abs(b-c))-1)
    except :
        break