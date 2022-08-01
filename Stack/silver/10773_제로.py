import sys
readline = sys.stdin.readline

k = int(readline())
stack = [0]

for _ in range(k) :
    next_number = int(readline())
    if next_number == 0 :
        stack.pop()
        continue
    stack.append(next_number)
print(sum(stack))