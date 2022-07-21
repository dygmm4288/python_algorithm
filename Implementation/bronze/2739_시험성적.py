import sys
readline = sys.stdin.readline

n = int(readline())

for i in range(1,10):
    print(f'{n} * {i} = {n*i}')