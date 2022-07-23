import sys
readline = sys.stdin.readline

n = int(readline())
for i in range(n) :
    printing = '*' * (n - i)
    print('%{0}s'.format(n)% printing)