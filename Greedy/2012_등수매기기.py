import sys
readline = sys.stdin.readline

N = int(readline())
ranking = []
for _ in range(N):
    ranking.append(int(readline()))
ranking.sort()

ret = 0
for i in range(N):
    ret += abs(i + 1 - ranking[i])
print(ret)

    