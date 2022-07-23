import sys
readline = sys.stdin.readline

ascending = '1 2 3 4 5 6 7 8'
descending = '8 7 6 5 4 3 2 1'

x = readline().strip()

if ascending == x :
    print('ascending')
elif descending == x :
    print('descending')
else :
    print('mixed')