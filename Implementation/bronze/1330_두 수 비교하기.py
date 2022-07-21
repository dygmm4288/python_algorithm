import sys
readline = sys.stdin.readline

a,b = map(int,readline().split())

ret = ''
if a > b : 
    ret = '>'
elif a < b :
    ret = '<'
else :
    ret = '=='
print(ret)