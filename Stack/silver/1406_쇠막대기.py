import sys
readline = sys.stdin.readline

left = list(readline().strip())
right = []

for _ in range(int(readline())) :
    cmd = readline().strip().split()
    if cmd[0] == 'L' :
        if left :
            right.append(left.pop())
    elif cmd[0] == 'D' : 
        if right :
            left.append(right.pop())
    elif cmd[0] == 'B' :
        if left :
            left.pop()
    elif cmd[0] == 'P' :
        left.append(cmd[1])
print(''.join(left+right[::-1]))
    