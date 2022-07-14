import sys 
readline = sys.stdin.readline

N, K = map(int,readline().split())

table = list(readline().strip())
ret = 0
inRange = lambda i : i >= 0 and i < N

for i in range(N):
    if table[i] == 'P' :
        for j in range(i-K,i+K+1):
            if inRange(j) and table[j] == 'H' :
                ret += 1
                table[j] = 'undefined'
                break
print(ret)