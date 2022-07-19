# n개의 버튼이 (일렬) 모두 불이 꺼진 상태
# 0 또는 1로 구성되어 있는 n자리 수
# 버튼을 눌르면 오른쪽 두개의 버튼도 눌린다
import sys
readline = sys.stdin.readline

n = int(readline())
next_state = list(map(int,readline().split()))
cur_state = [0] * n
ret = 0
change = lambda x : (x + 1) % 2
for i in range(n) :
    if next_state[i] != cur_state[i] :
        cur_state[i] = change(cur_state[i])
        if i + 1 < n : cur_state[i+1] = change(cur_state[i+1])
        if i + 2 < n : cur_state[i+2] = change(cur_state[i+2])
        ret += 1
print(ret)
          