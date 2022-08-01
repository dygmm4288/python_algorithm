import sys
readline = sys.stdin.readline

n = int(readline())
stack = []
for _ in range(n) :
    cmd = readline().strip().split()
    if len(cmd) > 1 : 
        stack.append(cmd[1])
    else :
        if cmd[0] == 'pop' :
            if stack : 
                print(stack.pop())
            else :
                print(-1)
        elif cmd[0] == 'size' :
            print(len(stack))
        elif cmd[0] == 'empty' :
            print(0 if len(stack) else 1)
        elif cmd[0] == 'top' :
            if stack : 
                print(stack[-1])
            else :
                print(-1)

