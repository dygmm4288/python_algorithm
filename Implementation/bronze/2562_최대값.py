import sys
readline = sys.stdin.readline
li = [int(readline()) for x in range(9)]
print(max(li),li.index(max(li)) + 1)
   