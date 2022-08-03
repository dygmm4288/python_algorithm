import sys
readline = sys.stdin.readline

expr = readline().strip()

stack = []
ret = ''
is_operator = lambda x : x == '(' or x == '*' or x == '/' or x == '+' or x == '-' or x == ')'
for s in expr :
    if is_operator(s) :
        if s == '*' or s == '/' :
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                ret += stack.pop()
        elif s == '+' or s == '-' or s == ')':
            while stack and stack[-1] != '(' :
                ret += stack.pop()
            if s == ')':
                stack.pop()
        if s != ')' :
            stack.append(s)
    else :
        ret += s
while stack :
    ret += stack.pop()
print(ret)