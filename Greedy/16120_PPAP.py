import sys
readline = sys.stdin.readline

S = readline().strip()
valid = lambda stack : stack[-4:] == ['P','P','A','P']

stack = []
for i in range(len(S)) :
    stack.append(S[i])
    if valid(stack) :
        for _ in range(3) :
            stack.pop()
if valid(stack) :
    for _ in range(3) :
        stack.pop()
print('PPAP' if stack[-1] == 'P' else 'NP')


    


