import sys
readline = sys.stdin.readline

n = int(readline())
li = sorted([int(readline()) for _ in range(n)])
for item in li :
  print(item)