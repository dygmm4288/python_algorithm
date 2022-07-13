import sys
readline = sys.stdin.readline
from queue import PriorityQueue

N = int(readline())
milks = PriorityQueue()
for i in range(N):
    milks.put(-int(readline()))
ret = 0
while not milks.empty() :
    # can divide with 3
    if milks.qsize() >= 3 :
        a = milks.get()
        b = milks.get()
        c = milks.get()
        ret += a + b
    # can't divide with 3
    else : 
        ret += milks.get()
print(-ret)

