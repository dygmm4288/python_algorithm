import sys

readline = sys.stdin.readline

while True:
    strings = readline()
    stack = []
    if strings == '.\n':
        break

    for s in strings:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                continue
            else: 
                stack.append(s)
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
                continue
            else:
                stack.append(s)
                break
    if stack : print('no')
    else : print('yes')