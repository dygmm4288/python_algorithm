import sys
readline = sys.stdin.readline

n = int(readline())
people = [list(map(int,readline().split())) for _ in range(n)]
ret = []
for p in people :
    [weight,height] = p
    k = 0
    for other in people :
        [o_weight,o_height] = other
        if weight == o_weight and height == o_height :
            continue
        if weight < o_weight and height < o_height:
            k += 1
    ret.append(k+1)
print(' '.join(map(str,ret)))