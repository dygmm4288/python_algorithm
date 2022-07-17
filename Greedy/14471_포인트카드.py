import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
cards = []

for _ in range(M):
    cards.append(list(map(int,readline().split())))

cards.sort(reverse=True,key=lambda x: x[0])
ret = 0
for card in cards :
    if M == 1 : break
     
    # if number of prize exceeds n, dont count
    if card[0] < N :
        ret += N - card[0]
    M -= 1
print(ret)
    