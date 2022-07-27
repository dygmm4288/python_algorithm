import sys
readline = sys.stdin.readline

n = int(readline())
ret = []
for i in range(n) :
    ret.append(' '* (n-i-1) + '*'*(2*i+1))

if n != 1 :ret += ret[n-2::-1]
for i in ret :
    print(i)