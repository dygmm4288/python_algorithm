import sys
readline = sys.stdin.readline

n = int(readline())

ret = 0
while n > 0 :
    if n % 5 == 0 :
        ret += n // 5
        n = 0
        break
    n -= 3
    ret += 1

print(ret if n == 0 else -1)        