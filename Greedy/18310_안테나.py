import sys
readline = sys.stdin.readline

N = int(readline())
homes = list(map(int,readline().split()))
homes.sort()

print(homes[(N-1)//2])