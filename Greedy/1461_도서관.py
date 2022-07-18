import sys
readline = sys.stdin.readline

n,m = map(int,readline().split())
pos = []
neg = []
for point in list(map(int,readline().split())) :
    if point >= 0 :
        pos.append(point)
    else :
        neg.append(-point)
pos.sort(reverse=True)
neg.sort(reverse=True)
MAX = max(
    pos[0] if len(pos)>0 else 0,
    neg[0] if len(neg)>0 else 0
)
ret = 0
for i in range(0,len(pos),m) :
    ret += pos[i] * 2
for i in range(0,len(neg),m) :
    ret += neg[i] * 2
ret -= MAX
print(ret)
    