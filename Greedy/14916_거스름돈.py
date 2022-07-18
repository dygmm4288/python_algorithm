import sys
readline = sys.stdin.readline

n = int(readline())
ret = 0
while n > 0 :
    if n % 5 == 0 :
        ret += n // 5 
        n //= 5
        break
    ret += 1
    n -= 2
print(-1 if n <0 else ret)
    