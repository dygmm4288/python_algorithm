import sys
readline = sys.stdin.readline

n,k = map(int,readline().split())
coins = [int(readline()) for _ in range(n)]
coins.sort(reverse=True)
ret = 0
for coin in coins :
    if coin <= k :
       ret += k // coin
       k -= (k//coin) * coin
print(ret)