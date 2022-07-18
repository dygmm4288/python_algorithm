import sys
readline = sys.stdin.readline

n,k = map(int,readline().split())
students = list(map(int,readline().split()))
cost = []
for i in range(0,n-1):
    cost.append(students[i+1] - students[i])
cost.sort(reverse=True)

ret = sum(cost)
for i in range(k-1) :
    ret -= cost[i]
print(ret)