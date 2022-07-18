#해결한 경우 파란색, 못한 경우 빨간색
#각 문제를 칠할 때 아래와 같은 과정을 한 번의 작업으로 수행
# 연속된 임의의 문제들을 선택
# 선택된 문제들을 전부 원하는 같은 색으로 칠한다.

import sys
readline = sys.stdin.readline

n = int(readline())
problems = readline().strip()

ret = 1
#colors[blue,red]
colors = [0,0]
sequence = []
cnt = 1
prev = problems[0]

for i in range(n):
    if problems[i] == 'B' :
        colors[0] += 1
    else :
        colors[1] += 1
    if prev == problems[i] :
        cnt += 1
    elif prev != problems[i] :
        prev = problems[i]
        sequence.append(cnt)
        cnt = 1
sequence.append(cnt)

print(ret + len(sequence) // 2)

...
#해결한 경우 파란색, 못한 경우 빨간색
#각 문제를 칠할 때 아래와 같은 과정을 한 번의 작업으로 수행
# 연속된 임의의 문제들을 선택
# 선택된 문제들을 전부 원하는 같은 색으로 칠한다.

import sys
readline = sys.stdin.readline

n = int(readline())
problems = readline().strip()

ret = 1
prev = problems[0]
cnt = 1
for i in range(n):
    if prev != problems[i] :
        prev = problems[i]
        cnt += 1
print(ret + cnt // 2)

...