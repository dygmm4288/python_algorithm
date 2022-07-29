import sys
readline = sys.stdin.readline

n,a,d = map(int,readline().split())

_next = a
ret = 0
for sound in list(map(int,readline().split())) :
    if sound == _next :
        ret += 1
        _next += d
print(ret)