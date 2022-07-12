import sys
readline = sys.stdin.readline
N, M = map(int,readline().split())
J = int(readline())

pos = 1
ret = 0

for _ in range(J):
    next_pos = int(readline())

    if next_pos < pos:
        ret += abs(next_pos - pos)
        pos = next_pos
        
    elif next_pos > pos + M -1:
        ret += abs(next_pos - (pos+M-1))
        pos = next_pos - M + 1
print(ret)
    