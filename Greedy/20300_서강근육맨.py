# pt를 받을 때마다 최대 2개까지만 선택할 수 있다.
# N개의 기구를 한번씩 사용 하고 싶음
# 비용 절약을 위해 pt를 받을 때 운동기구를 되도록이면 2개
# pt를 받을 때 마다 근손실 정도가 m을 넘지 않도록 하고 싶다
# 이 때 m의 최솟값을 구해보자
# 운동기구 2개를 사용해서 근손실 정도는 두 운동기구의 근손실 정도의 합이다.
# m을 최소화 하려면... 최대값과 최소값을 더하면 되지 않나..
# 최대값 두개는 너무 확 뛸 것 같고

import sys
readline = sys.stdin.readline

n = int(readline())
equipments = list(map(int,readline().split()))
equipments.sort()
#n이 짝수이면
ret = 0
if n % 2 == 0 :
    #짝수면 무조건 2개식 엮어야 한다
    for i in range(n//2) :
        ret = max(ret,equipments[i] + equipments[n-i-1])
#n이 홀수이면
else :
    #무조건 하나가 남는데...
    ret += equipments.pop()
    for i in range((n-1)//2) :
        ret = max(ret,
                  equipments[i] + equipments[n-i-2])
print(ret)