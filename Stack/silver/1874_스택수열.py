import sys
readline = sys.stdin.readline

n = int(readline())

stack = []
ret = []
cur = 1
for _ in range(n) :
    num = int(readline())
    #일단 숫자가 나올 때 까지 넣고
    while cur <= num :
        stack.append(cur)
        cur += 1
        ret.append('+')
    top = stack[-1]
    if top != num : 
        print('NO')
        sys.exit(0)
    stack.pop()
    ret.append('-')
for s in ret :
    print(s)
     
   