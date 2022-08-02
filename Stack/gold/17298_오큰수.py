import sys
readline = sys.stdin.readline

n = int(readline())
seq = list(map(int,readline().split()))

stack = []
for i,item in enumerate(seq) :
    while stack and item > seq[stack[-1]] :
        seq[stack.pop()] = item
    stack.append(i)

while stack :
    seq[stack.pop()] = -1
print(' '.join(map(str,seq)))
  