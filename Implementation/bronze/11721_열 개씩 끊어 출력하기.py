import sys
readline = sys.stdin.readline

words = readline().strip()

ret = ''
for i in range(len(words) // 10 + 1) :
    ret += words[i*10:i*10+10] + '\n'
print(ret)

