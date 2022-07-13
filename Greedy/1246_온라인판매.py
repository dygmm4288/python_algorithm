import sys
readline = sys.stdin.readline

N, M = map(int,readline().split())
P = [0] * M
for i in range(M):
    P[i] = int(readline())
P.sort()
# [책정금액,총 수익]
best = [0,0]

for i in range(M):
    # 뒤에 있을 P[i]는 현재 금액보다 작다
    # 현재 있는 사람 포함 뒤에 있는 사람이 다 살 경우 금액
    # M - i
    # 달걀 수 보다는 작아야 됨
    cand_price = min(N*P[i],(M-i)*P[i])
    print(cand_price)
    if best[1] < cand_price :
        best[0] = P[i]
        best[1] = cand_price
print(' '.join(map(str,best)))
    