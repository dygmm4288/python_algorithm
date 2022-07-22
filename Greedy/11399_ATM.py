import sys
readline = sys.stdin.readline

n = int(readline())
people = list(map(int,readline().split()))
people.sort()

psum = 0
ret = 0
for p in people :
    ret += p + psum
    psum += p
print(ret)
    