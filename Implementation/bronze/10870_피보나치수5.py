import sys
readline = sys.stdin.readline

n = int(readline())
if n == 0 :
    print(0)
    sys.exit(0)
def fibo(x) :
    if x <= 2 : return 1
    else : return fibo(x-1) + fibo(x-2)
print(fibo(n))