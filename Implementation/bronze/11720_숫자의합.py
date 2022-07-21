import sys
readline = sys.stdin.readline
ret = 0
n = int(readline())
number = readline().strip()
for string_value in number :
    ret += int(string_value)
print(ret)
    


