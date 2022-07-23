import sys
readline = sys.stdin.readline

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z='];

word = readline().strip()

ret = len(word)

for c in croatia :
    ret -= word.count(c)
print(ret)