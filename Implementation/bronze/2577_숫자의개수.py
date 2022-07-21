import sys
readline = sys.stdin.readline

a = int(readline())
b = int(readline())
c = int(readline())

count = [0] * 10

for n in str(a * b * c) :
    count[int(n)] += 1
for i in range(10):
    print(count[i])