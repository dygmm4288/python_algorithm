# 정상가격의 75%
# 모든 물건의 정상가는 4의 배수인 정수 할인된 가격도 모두 정수
import sys
readline = sys.stdin.readline

for i in range(int(readline())) :
    n = int(readline())
    prices = list(map(int,readline().split()))
    # 할인 가격에 해당하는 오름차순으로 정렬된 n개의 정수
    # 제일 큰 가격은 할인된 가격이 아니다
    ret = []
    while prices :
        top = prices.pop()
        ret.append(
          prices.pop(
            prices.index(
              int(top*0.75)
            )
          )
        )
        
    print(f'Case #{i+1}: {" ".join(map(str,ret[::-1]))}')
    