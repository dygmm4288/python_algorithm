import sys
readline = sys.stdin.readline

n = int(readline())
last_come, fastest_leave = 0, 987654321
for _ in range(n):
    [start,end] = list(map(int,readline().split()))
    last_come = max(last_come,start)
    fastest_leave = min(fastest_leave,end)
gap = last_come - fastest_leave
print(gap if gap > 0 else 0)
    