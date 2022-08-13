import sys
readline = sys.stdin.readline

while True :
    data = list(map(int,readline().split()))
    n = data[0]
    if n == 0 :
        break
    heights = data[1:]
    heights.append(0)
    stack = []
    ret = 0
    for i in range(n+1) :
        while stack and heights[stack[-1]] >= heights[i] :
            j = stack.pop()
            if not stack :
                width = i
            else :
                width = i - stack[-1] - 1
            ret = max(ret,width*heights[j])
        stack.append(i)
    print(ret)