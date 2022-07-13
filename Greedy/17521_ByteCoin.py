import sys
readline = sys.stdin.readline

n, W = map(int,readline().split())

coin_price = [0] * n

for i in range(n):
    coin_price[i] = int(readline())

for i in range(n-1):
    prev = coin_price[i]
    next = coin_price[i+1]
    if prev < next :
       W = (W//prev) * next + (W % prev)
print(W)