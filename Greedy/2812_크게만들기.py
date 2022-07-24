import sys
readline = sys.stdin.readline

n,k = map(int,readline().split())
number = readline().strip()

stack = []
ret = 0
for num in number :
    while ret < k and stack and stack[-1] < int(num) :
        stack.pop()
        ret += 1
    stack.append(int(num))
while ret < k :
    stack.pop()
    k -= 1
print(''.join(map(str,stack)))