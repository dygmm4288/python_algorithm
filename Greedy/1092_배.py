# 이거 실행시간 python으로 하면 안되고
# pypy로 하니까 됨..

import sys
readline = sys.stdin.readline

n = int(readline())
cranes = list(map(int,readline().split()))
m = int(readline())
boxes = list(map(int,readline().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0] :
    print(-1)
else :
    ret = 0
    while len(boxes) > 0 :
        for crane in cranes :
            for box in boxes :
                if box <= crane  :
                    boxes.remove(box)
                    break
                    
        ret +=1
    print(ret)   
        