import sys
readline = sys.stdin.readline
def mul(a,b) :
    return a * b
T = int(readline())

for _ in range(T):
    j, N = map(int,readline().split())
    boxes = []
    for _ in range(N):
        boxes.append(mul(*map(int,readline().split())))
    boxes.sort(reverse=True)
    sum_boxes = [boxes[0]]
    ret = 1
    for i in range(1,N):
        if sum_boxes[i-1] >= j : break
        sum_boxes.append(sum_boxes[i-1] + boxes[i])
        ret += 1
    print(ret)
    