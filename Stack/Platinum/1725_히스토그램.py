import sys
readline = sys.stdin.readline

n = int(readline())
array = [int(readline()) for _ in range(n)]
array.append(0)
stack = []

ret = 0
for i in range(n+1) :
    # 처리되지 않은 막대가 있고
    # 처리되지 않은 막대 중 마지막 막대가 현재 막대보다 큰경우
    # 처리 되지 않은 막대는 너비를 알 수 있다.
    while stack and array[stack[-1]] >= array[i] :
        j = stack.pop()
        # array[j] 기준 오른쪽은 i이다
        right = i
        # array[j] 기준 왼쪽은 처리되지 않은 막대 중 왼쪽인데
        # 남아 있는 막대가 없으면
        # left는 현재 인덱스보다 
        if not stack :
            width = i
        else :
            width = right - stack[-1] - 1
        ret = max(ret,width*array[j])
    stack.append(i)
print(ret)