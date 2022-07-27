import sys
readline = sys.stdin.readline

n = int(readline())
ret = []
for i in range(n) :
    ret.append('*' * (i+1))

if n != 1 :ret += ret[n-2::-1]
for i in ret :
    print(i)