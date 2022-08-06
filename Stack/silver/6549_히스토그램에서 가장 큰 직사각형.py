import sys
readline = sys.stdin.readline

def solveStack(h) :
    remaining = []
    h.append(0)
    ret = 0
    for i in range(len(h)) :
        while remaining and h[remaining[-1]] >= h[i] :
            j = remaining.pop()
            width = -1
            
            if not remaining :
                width = i
            else :
                width = (i - remaining[-1] - 1)
            ret = max(ret,h[j]*width)
        remaining.append(i)
    return ret

        
while True :
    h = list(map(int,readline().split()))
    if h[0] == 0 :
        break
    print(solveStack(h))


