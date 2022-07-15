import sys
readline = sys.stdin.readline

L, R = map(list,readline().split())

ret = 0
if len(L) == len(R) :
    for i in range(len(L)) :
        if L[i] != R[i] : break
        if L[i] == R[i] and L[i] == '8' :
            ret += 1
print(ret)