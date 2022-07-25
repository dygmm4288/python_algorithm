import sys
readline = sys.stdin.readline

n = int(readline())

fibo = [0,1]
for i in range(2,46) :
    fibo.append(fibo[i-1] + fibo[i-2])
print(fibo[n])