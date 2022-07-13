import sys
readline = sys.stdin.readline

from collections import deque

T = int(readline())

for _ in range(T):
    N = int(readline())
    cards = readline().split()
    pivot = cards[0]
    dq = deque([cards[0]])
    for i in range(1,N):
      # push left
      if pivot >= cards[i] :
          dq.appendleft(cards[i])
          pivot = cards[i]
      else :
          dq.append(cards[i])
    print(''.join(dq))