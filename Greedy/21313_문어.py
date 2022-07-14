import sys
readline = sys.stdin.readline

n = int(readline())

ret = [1,2] * (n // 2)
if n % 2 != 0 :
    ret.append(3)
print(' '.join(map(str,ret)))
# or print(*ret) * is splat operator