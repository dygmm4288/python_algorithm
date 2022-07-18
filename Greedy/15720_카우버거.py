# 버거 1, 사이드 1, 음료 1 -> 각 제품에 대해 10퍼센트 할인
# 버거 * 0.9 + 사이드 *0.9 + 음료 * 0.9
import sys
readline = sys.stdin.readline

B,C,D = map(int,readline().split())
burgers = list(map(int,readline().split()))
sides = list(map(int,readline().split()))
drinks = list(map(int,readline().split()))

total = sum(burgers) + sum(sides) + sum(drinks)

# 최대 할인을 받기 위해서는..
# 세트가 이뤄지지 않을 수도 있다
# 따라서 최대한 큰 액수를 할인을 해야 할인율이 높아진다
burgers.sort(reverse=True)
sides.sort(reverse=True)
drinks.sort(reverse=True)
ret = 0
get = lambda x,i : int(x[i] * 0.9)
min_length = min(B,C,D)
for i in range(min_length):
    ret += get(burgers,i)
    ret += get(sides,i)
    ret += get(drinks,i)

  
sum_rest = lambda length : lambda li : sum([x for x in li[length:]])
sum_min_rest = sum_rest(min_length)

ret += sum_min_rest(burgers)
ret += sum_min_rest(sides)
ret += sum_min_rest(drinks)

print(total)
print(ret)