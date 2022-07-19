# 처음과 마지막이 아닌 탑 중 하나를 선택한다. 단, 선택한 탑과 인접한 두 탑의 높이가 모두 1이상이어야 한다
# 선택한 탑과 인접한 두 탑에 있는 블롭을 한마리씩 각각 땅에 내려 놓는다 
# tower[i],tower[i+1],tower[i-1] -= 1
# 땅에 내려놓은 블롭 중 하나의 블롭만 선택한 탑에 쌓는다
# tower[i] += 1

import sys
readline = sys.stdin.readline

n = int(readline())
towers = list(map(int,readline().split()))
ret = 0 
for i in range(1,n-1) :
    ret = max(ret,towers[i] + min(towers[i-1],towers[i+1]))
ret = max(ret,towers[0],towers[n-1])
print(ret)