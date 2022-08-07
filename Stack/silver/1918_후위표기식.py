import sys
readline = sys.stdin.readline

expr = readline().strip()

stack = []
ret = ''
is_operator = lambda x : x == '(' or x == '*' or x == '/' or x == '+' or x == '-' or x == ')'
for s in expr :
    if is_operator(s) :
        # 우선순위가 + - 보다 높은 것 부터
        if s == '*' or s == '/' :
            # stack에 원소가 있고, 마지막이 * 혹은 / 일때까지 
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                ret += stack.pop()
        elif s == '+' or s == '-' or s == ')':
            # 괄호 내에 있는건 무조건 빼버린다
            while stack and stack[-1] != '(' :
                ret += stack.pop()
            if s == ')':
                stack.pop()
        if s != ')' :
            # 나머지 숫자일 경우 스택에 넣는다
            stack.append(s)
    else :
        ret += s
while stack :
    ret += stack.pop()
print(ret)