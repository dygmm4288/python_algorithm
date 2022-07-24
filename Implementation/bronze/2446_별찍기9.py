import sys
readline = sys.stdin.readline

n = int(readline())
printing = []

ret = '*'

for i in range(n) :
    blank = ' '*(n-i-1)
    blank += ret
    printing.append(blank)
    ret += '**'
printing.reverse()
for i in range(n-1) :
    printing.append(printing[n-i-2])
for ret in printing :
    print(ret)