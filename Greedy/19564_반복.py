import sys
readline = sys.stdin.readline

words = [123] + list(map(ord,readline().strip()))
ret = 0
#find value more than next value
for i in range(len(words)-1) :
    # if equal or greater than next value, press button
    if words[i] >= words[i+1] :
        ret += 1
print(ret)