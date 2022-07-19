import sys
readline = sys.stdin.readline

n = int(readline())
players = list(map(int,readline().split()))
me = players[0]
players = players[1:]

players.sort()

flag = True

for player in players:
    if me > player : 
        me += player
    elif me < player:
        flag = False
        break
print('Yes' if flag else 'No')
    

