import sys
readline = sys.stdin.readline

n = int(readline())
heights = [tuple(map(int,readline().split())) for _ in range(n)]

heights.sort(key=lambda x: x[0])

stack = []
ret = 0
for i in range(n) :
    if not stack :
        stack.append(heights[i])
    else :
        if stack[-1][1] <= heights[i][1] :
            left = stack.pop()
            ret += (heights[i][0] - left[0]) * left[1]
            stack.append(heights[i])
if stack :ø
    top = stack.pop()
    ret += top[1]
stack = []
for i in range(n-1,-1,-1) :
    if not stack:
        stack.append(heights[i])
    else :
        if stack[-1][1] < heights[i][1] :
            right = stack.pop()
            ret += (right[0] - heights[i][0]) * right[1]
            stack.append(heights[i])
print(ret)