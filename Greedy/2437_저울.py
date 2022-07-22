import sys
readline = sys.stdin.readline

n = int(readline())
weights = sorted(list(map(int,readline().split())))


if weights[0] > 1 :
    print(1)
    sys.exit(0)

psum = 1
for weight in weights :
    if psum >= weight :
        psum += weight
    elif psum < weight :
        break
print(psum)

        
        