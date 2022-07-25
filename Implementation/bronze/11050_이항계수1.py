import sys
readline = sys.stdin.readline

n,k = map(int,readline().split())

def factorial(n) :
    if n <= 1 : return 1
    return n * factorial(n-1)
def bino(n,k) :
    if k < 0 : return 0
    elif k > n : return 0
    else: return factorial(n) // (factorial(k)*factorial(n-k))
print(bino(n,k))
