import sys
readline = sys.stdin.readline

opening = list(map(lambda x : x % ord('A'),map(ord,readline().strip())))
ret = 0
# start at A
cur_pos = 0
for next_pos in opening:
    # min(clockwise,anticlockwise)
    ret += min(
        abs(next_pos - cur_pos),
        abs(26 - abs(next_pos-cur_pos))
    )
    cur_pos = next_pos
print(ret)