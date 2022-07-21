#n개의 나무가 있는데, 하루에 한 나무씩 n일 산에 오르며 나무를 잘라갈것이다
# 어느 나무를 먼저 잘라가느냐에 따라서 총 구할 수 있는 양이 다른데
# 영선이가 얻을 수 있는 최대 나무양을 구하시오
# 최대한 많은 나무를 얻기 위해서는
# 가장 빨리 자라나는 나무를 먼저 친다.. => 밤이 지나야 자라나기 때문에 그전에 더 많이 자란 나무가 있을 것이다.
# 현재 기준에서 가장 많이 자란 나무를 친다
# 1<=n<= 100000
# 가장 빨리 자라는 나무를 가장 나중에 친다
# 짧은 것부터 치고 그 다음에 가장 커졌을 때 나무를 친다
import sys
readline = sys.stdin.readline

n = int(readline())
h = list(map(int,readline().split()))
a = list(map(int,readline().split()))
trees = []
for i in range(n):
    trees.append([h[i],a[i]])
trees.sort(key=lambda x : x[1])
ret = 0
for day in range(n) :
    ret += trees[day][0] + (trees[day][1] * day)
print(ret)
