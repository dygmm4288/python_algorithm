# print 방법
coins = [25,10,5,1]
T = int(input())
for _ in range(T):
    N = int(input())
    ret = []
    for coin in coins:
        ret.append(str(N//coin))
        N %= coin
    print(' '.join(ret))


        
        