
# 연속된 두 일자에 각각 일정이 1개 이상 있다면 이를 일정이 연속됐다
# 연속된 모든 일정은 하나의 직사각형에 포함되어야 한다
# 연속된 일정을 모두 감싸는 가장 작은 직사각형의 크기만큼 코팅지를 오린다

import sys
readline = sys.stdin.readline

n = int(readline())
MAX = 365 + 2
days = [0] * MAX

for _ in range(n) :
    s,e = map(int,readline().split())
    days[s] += 1
    days[e+1] -= 1

for i in range(1,MAX) :
    days[i] += days[i-1]
  
ret = 0
cnt = 0
height = 0

for i in range(MAX):
    if days[i] == 0 :
        ret += height * cnt
        cnt = 0
        height = 0
    elif days[i] != 0 :
        cnt += 1
        height = max(height,days[i])
print(ret)
        