import sys
readline = sys.stdin.readline

n = readline()

next_state = n
ret = 1
if int(next_state) < 10 :
    next_state = '0' + next_state
sumFirst = int(next_state[0]) + int(next_state[1])
next_state = next_state[1] + str(sumFirst)[-1]

while int(next_state) != int(n) :
    sumFirst = int(next_state[0]) + int(next_state[1])
    next_state = next_state[1] + str(sumFirst)[-1]
    ret += 1
print(ret)

