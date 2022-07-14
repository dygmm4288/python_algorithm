import sys
readline = sys.stdin.readline

N = int(readline())

sides = [0] * N
for i in range(N):
    sides[i] = int(readline())
sides.sort(reverse=True)
best = -1
# a - b < c < a + b (c > a > b)
for i in range(N-2):
    c = sides[i]
    for j in range(i+1,N-1):
        a = sides[j]
        b = sides[j+1]
        if a - b < c and c < a + b and best < a + b + c :
            best = a + b + c
            break
    if best != -1 :
        break
print(best)

