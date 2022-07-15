import sys 
readline = sys.stdin.readline


T = int(readline())
# Set fibo 
MAX_NUM = 50
fibo = [0] * MAX_NUM
fibo[0] = 1
fibo[1] = 1
for i in range(2,MAX_NUM):
    fibo[i] = fibo[i-1] + fibo[i-2]

def search(n,fibo) :
    lo, hi = 0, MAX_NUM
    while lo < hi :
        mid = (lo+hi)//2
        if fibo[mid] > n : hi = mid
        else : lo = mid + 1
    return lo - 1
    
for _ in range(T):
    n = int(readline())
    ret = []
    while n != 0 :
        temp_index = search(n,fibo)
        n -= fibo[temp_index]
        ret.append(fibo[temp_index])
    ret.reverse()
    print(' '.join(map(str,ret)))