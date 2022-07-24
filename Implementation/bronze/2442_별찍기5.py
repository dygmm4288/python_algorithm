import sys
readline = sys.stdin.readline

n = int(readline())
ret = '*'

for i in range(n) :
    blank = ' ' * (n - i-1)
    blank += ret
    print(blank)
    ret += '**'
  
