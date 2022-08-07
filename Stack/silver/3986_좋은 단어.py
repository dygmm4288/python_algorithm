import sys

readline = sys.stdin.readline

n = int(readline())
ret = 0
for _ in range(n):
    S = readline().strip()
    stack = []
    for s in S:
        if stack and s == stack[-1]:
            stack.pop()
            continue
        stack.append(s)

    if not stack: ret += 1
print(ret)
