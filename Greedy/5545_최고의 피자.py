# 피자 가격 = 도우 가격 + (토핑 가격 * k 종류) 
# 피자의 열량 = 도우 + 토핑의 열량의 합

# 1원당 열량이 가장 높은 피자를 확인하기 위해서는 (열량 / 가격)

# 최고피자 -> (도우 열량 + sum(토핑 열량들)) / 도우가격 +토핑가격 * k종류
# sum(토핑 열량들)은 높아야 돼 -> 높은것부터 선택
import sys
readline = sys.stdin.readline

n = int(readline())
a, b = map(int,readline().split())

c = int(readline())

toppings = []
for _ in range(n) :
    toppings.append(int(readline()))

toppings.sort(reverse=True)

sum_toppings = [toppings[0]]

for i in range(n-1) :
    sum_toppings.append(toppings[i+1] + sum_toppings[i])

# 토핑 선택 안한 결과
best = a // c
for i in range(n) :
  best = max(best, (c + sum_toppings[i]) // (a + b *(i+1)))
print(best)