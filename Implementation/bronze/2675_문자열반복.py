import sys
readline = sys.stdin.readline
for _ in range(int(readline())) :
    R,S = readline().strip().split()
    R = int(R)
    P = ''
    for s in S :
        temp = s * R
        P += temp
    print(P)