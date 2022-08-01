import sys
readline = sys.stdin.readline
from functools import cmp_to_key

n = int(readline())
numbers = readline().strip().split()

def compare(a,b) :
    aplusb = a+b
    bplusa = b+a
    return int(bplusa) - int(aplusb)
numbers.sort(key=cmp_to_key(compare))
ret = ''.join(map(str,numbers))
if ret == ('0' * len(ret)) : print(0)
else : print(ret)