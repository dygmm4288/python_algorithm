import sys
readline = sys.stdin.readline

n = int(readline())
heights = list(map(int,readline().split()))

_sum = 0
_count =0
for height in heights :
    _sum += height
    _count += height // 2

if _sum % 3 != 0 : 
    print('NO')
else :
    if _count >= (_sum//3) :
        print('YES')
    else :
        print('NO')