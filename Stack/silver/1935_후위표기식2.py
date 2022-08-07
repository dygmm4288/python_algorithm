import sys
readline = sys.stdin.readline
 
n = int(readline())
alpha = [0] * 26
li = readline().rstrip();
for i in range(n) :
    alpha[i] = int(readline())
stack = []
for s in li :
    if s == '+' or s == '-' or s == '/' or s =='*' :
        b = stack.pop()
        a = stack.pop()
        if s == '+' :
            stack.append(a+b)
        elif s == '-' :
            stack.append(a-b)
        elif s == '/' :
            stack.append(a/b)
        else :
            stack.append(a*b)
    else :
        stack.append(alpha[ord(s)-ord('A')])

print(format(stack[0],'.2f'))