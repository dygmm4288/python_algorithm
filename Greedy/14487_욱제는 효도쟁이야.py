N = int(input())
costs = list(map(int,input().split()))

ret = 0
costs.sort()

for i in range(N-1):
    ret += costs[i]
  
print(ret)