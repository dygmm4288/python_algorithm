import sys
readline = sys.stdin.readline

n = int(readline())
sticks = [int(readline()) for _ in range(n)]

ret = 0
height = 0
while sticks :
    stick = sticks.pop()
    if height < stick :
        height = stick
        ret += 1
print(ret)