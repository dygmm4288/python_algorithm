import sys
readline = sys.stdin.readline

strings = readline().strip()
stack = []
for s in strings : 
    if s == '(' or s== '[' :
        stack.append(s)
    elif s == ')':
        # '()'일때
        if stack and stack[-1] == '(':
            stack.pop()
            stack.append(2)
            continue
        # 올바른 괄호가 아닐 때
        if not stack or stack[-1] == '[':
            print(0)
            sys.exit(0)
        # '(x...)' 일때
        temp = 0
        while stack and stack[-1] != '(' and stack[-1] != '[':
            temp += stack.pop()
        if not stack or stack[-1] == '[' :
            print(0)
            sys.exit(0)
        elif stack and stack[-1] == '(':
            stack.pop()
            stack.append(temp*2)
    elif s == ']' :
        if stack and stack[-1] == '[':
            stack.pop()
            stack.append(3)
            continue
        if not stack or stack[-1] == '(':
            print(0)
            sys.exit(0)
        temp = 0
        while stack and stack[-1] != '(' and stack[-1] != '[' :
            temp += stack.pop()
        if not stack or stack[-1] == '(':
            print(0)
            sys.exit(0)
        elif stack and stack[-1] == '[':
            stack.pop()
            stack.append(temp*3)
ret = 0
while stack :
    if stack[-1] == '(' or stack[-1] == '[' :
        ret = 0
        break
    ret += stack.pop()
print(ret)
        
            
        
        