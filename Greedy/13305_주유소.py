N = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

here = 0
ret = 0
best = 1000000001

while here < N-1:
  if best > price[here]:
     best = price[here]
     ret += distance[here] * price[here]
  else :
    ret += distance[here] * best
  here += 1
print(ret)