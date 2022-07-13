import sys
readline = sys.stdin.readline

N = int(readline())
customers = [0] * N
for i in range(N):
    customers[i] = int(readline())
customers.sort(reverse=True)

ret = 0
for i in range(N):
    if customers[i] - i > 0 :
        ret += customers[i] - i
print(ret)