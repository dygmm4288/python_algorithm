import sys
readline = sys.stdin.readline

MAX = 21
factorials = [1] * MAX
for i in range(1,MAX) :
    for j in range(1,i+1) :
        factorials[i] *= j
n = int(readline())
if n == 0 :
    print('NO')
    sys.exit(0)
def search(li,value) :
    lo,hi = 0, MAX
    while lo < hi :
        mid = (lo+hi)//2
        if li[mid] > value : hi = mid 
        else : lo = mid + 1
    return lo -1
used = [False] * MAX
while n > 0 :
    temp_index = search(factorials,n)
    if temp_index <= 2 and used[temp_index] :
        temp_index -= 1 
    if temp_index < 0 : break
    if(used[temp_index]) :break
    n -= factorials[temp_index]
    used[temp_index] = True
print('YES' if n == 0 else 'NO')