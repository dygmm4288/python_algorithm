import sys
readline = sys.stdin.readline

n = int(readline())
sticks = list(map(int,readline().split()))

sticks.sort(reverse=True)

next_sticks = sum(sticks)
ret = 0

for i in range(n-1) :
    ret += (next_sticks - sticks[i]) * sticks[i]
    next_sticks -= sticks[i]
print(ret)
    
    



