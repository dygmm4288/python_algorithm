N, M = map(int,input().split())
ret = 0 
if N == 1 : 
    ret = 1
elif N == 2 :
    ret = min(4,(M+1) // 2)
elif M < 7 :
    ret = min(4,M)
else :
    ret = M - 2
print(ret)