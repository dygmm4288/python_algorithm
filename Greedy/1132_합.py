import sys
readline = sys.stdin.readline

n = int(readline())
A = ord('A')
alpha = [[0,False] for _ in range(10)]

for _ in range(n) :
    number = readline().strip()
    l = len(number)
    alpha[ord(number[0])-A][1] = True
    for i,value in enumerate(number):
        alpha[ord(value) - A][0] += (10 ** (l - i))
alpha.sort(reverse=True)

if alpha[-1][1] :
    for i in range(9,-1,-1) :
        if not alpha[i][1] :
            del alpha[i]
            break

next_number = 9
ret = 0
for value in alpha :
    if value[0] != 0 :
        ret += next_number * (value[0] // 10)
        next_number -= 1
print(ret)

