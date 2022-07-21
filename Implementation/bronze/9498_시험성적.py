import sys
readline = sys.stdin.readline

score = int(readline())
ret = ''
if score >= 90 :
    ret = 'A'
elif score >= 80 :
    ret = 'B'
elif score >= 70 :
    ret = 'C'
elif score >= 60:
    ret = 'D'
else :
    ret = 'F'
print(ret)