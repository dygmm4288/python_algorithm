import sys
readline = sys.stdin.readline

inputs = readline().strip()
inputs = inputs.replace('()','0')

stack = []
ret = 0
for i, s in enumerate(inputs) :
    if s == '(' :
        stack.append(i)
    elif s== ')' :
        left = stack.pop()
        right = i
        ret += inputs[left:right].count('0') + 1
      
print(ret)
            



