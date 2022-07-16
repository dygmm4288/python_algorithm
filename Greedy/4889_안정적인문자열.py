import sys
readline = sys.stdin.readline
test_case = 1
while True :
    s = readline().strip()
    if '-' in s :
        break
    stack = []
    ret = 0
    for i in range(len(s)) :
        if s[i] == '{' :
            stack.append(s[i])
        else :
            if not stack:
                stack.append('{')
                ret += 1
            else :
                stack.pop()
    while stack:
        a = stack.pop()
        b = stack.pop()
        if a == b :
            ret +=1
        else :
            ret += 2
    print(f'{test_case}. {ret}')
    test_case += 1
  
        