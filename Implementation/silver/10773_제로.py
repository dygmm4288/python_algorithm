import sys
readline = sys.stdin.readline

k = int(readline())
# 정수가 "0"일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다
# 정수가 "0일" 경우에는 지울 수 있는 수가 있음을 보장할 수 있다.
stack = []
for _ in range(k):
    num = int(readline())
    if num == 0 :
        stack.pop()
        continue
    stack.append(num)
print(sum(stack))