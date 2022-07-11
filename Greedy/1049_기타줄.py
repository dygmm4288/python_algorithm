# needed guitar strings is N
# number of brande is M
N, M = map(int,input().split())

brandes = []

for _ in range(M):
    brandes.append(list(map(int,input().split())))
ret = 0
while N > 0:
    min_value = 987654321
    if N >= 6:
        for brand in brandes:
            min_value = min(min_value,
                            brand[0],
                            brand[1] * 6)
    else :
        for brand in brandes:
            min_value = min(min_value,
                            brand[0],
                            brand[1] * (N%6))
    ret += min_value
    N -= 6

print(ret)
        
    
