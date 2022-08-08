import sys,collections
readline = sys.stdin.readline

q = collections.deque()
n,k = map(int,readline().split())
for i in range(n) :
    q.append(i+1)
ret =[]
while len(q) > 1 : 
    _next = k
    while _next-1 != 0 :
        q.append(q.popleft())
        _next -= 1
    ret.append(q.popleft())
if q :
    ret.append(q.popleft())

print('<'+', '.join(map(str,ret))+'>')
