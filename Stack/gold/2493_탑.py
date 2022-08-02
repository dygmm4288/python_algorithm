import sys
readline = sys.stdin.readline

n = int(readline())
towers = list(map(int,readline().split()))

stack = []

for i in range(n-1,-1,-1) :
    while stack and towers[stack[-1]] <= towers[i] :
        towers[stack.pop()] = i+1
    stack.append(i)
while stack :
    towers[stack.pop()] = 0
print(' '.join(map(str,towers)))

    