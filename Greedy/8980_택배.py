import sys
readline = sys.stdin.readline

n,c = map(int,readline().split())
m = int(readline())
delivery = [c] * (n + 1)
boxes = [list(map(int,readline().split())) for _ in range(m)]

boxes.sort(key=lambda x : x[1])
ret = 0

for a,b,c in boxes :
    _min = min(*delivery[a:b],c)
    for i in range(a,b) :
        delivery[i] -= _min
    ret += _min
print(ret)
    


