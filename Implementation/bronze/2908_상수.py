import sys
readline = sys.stdin.readline

a,b = map(lambda x : x[::-1],readline().split())
print(a if int(a) > int(b) else b)