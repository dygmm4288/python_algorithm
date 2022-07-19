import sys
readline = sys.stdin.readline

cur_state = ['N'] + list(readline().strip())
n = len(cur_state)
next_state = ['N'] * n
change = lambda x : 'Y' if x == 'N' else 'N'

ret = 0
for i in range(1,n):
    if cur_state[i] == 'Y':
        for j in range(i,n,i) :
          cur_state[j] = change(cur_state[j])
        ret += 1
print(ret if cur_state == next_state else -1)
       