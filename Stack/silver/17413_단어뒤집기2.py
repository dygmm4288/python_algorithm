import sys
readline = sys.stdin.readline

S = readline().strip()
ret = ''
stack = []
tag = False
for s in S :
    if not tag :
        if s == '<' :
            while stack :
                ret += stack.pop()
            tag = True
            ret += s
        elif s != ' ' :
            stack.append(s)
        elif s == ' ' :
            while stack :
                ret += stack.pop()
            ret += s
    elif tag :
        if s != '>' :
            ret += s
        elif s == '>' :
            tag = False
            ret += s
while stack :
    ret += stack.pop()
print(ret)