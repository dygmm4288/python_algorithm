from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()

# Push the value on PriorityQueue
for _ in range(N):
    pq.put(int(input()))

# Always plus two min values
ret = 0
while pq.qsize() > 1:
    a = pq.get()
    b = pq.get()
    ret += a + b
    pq.put(a+b)

print(ret)

