import sys
readline = sys.stdin.readline

T = int(readline())
for _ in range(T) :
    n = int(readline())
    price = list(map(int,readline().split()))
    max_price = price[n-1]
    ret = 0
    for i in range(n):
        if max_price < price[n-i-1]:
            max_price = price[n-i-1]
        elif max_price > price[n-i-1]:
            ret += max_price - price[n-i-1]
    print(ret)
    