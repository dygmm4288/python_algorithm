import sys
readline = sys.stdin.readline

'''
    폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며 남은 문자열은 합쳐지게 된다
    1. 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다.
    남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다
    2. 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
    3. 폭발은 폭발 문자열이 문자열에 없을 때 까지 반복된다.
'''
S = readline().strip()
explode = readline().strip()
stack = []
n = len(explode)
for s in S :
    stack.append(s) 
    
    if explode[-1] == stack[-1] and ''.join(stack[-n:]) == explode :
        for _ in range(n) :
            if stack :
                stack.pop()
ret = ''.join(stack)
if len(ret) == 0  : print('FRULA')
else : print(ret)