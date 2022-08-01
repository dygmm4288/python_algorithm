import sys
readline = sys.stdin.readline

n = int(readline())

def valid(ps) :
    stack = []
    for s in ps :
        if s == '(' :
            stack.append(s)
        else :
            if len(stack) >= 1 :
                stack.pop()
            else :
                return 'NO'
    if len(stack) != 0  : return 'NO'
    return 'YES'

for _ in range(n) :
    ps = readline().strip()
    print(valid(ps))