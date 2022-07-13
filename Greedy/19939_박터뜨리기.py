N, K = map(int,input().split())

sum = 0
diff = K - 1
for i in range(K):
    sum += i+1
if sum > N : print(-1)
else :
    if (N - sum) % K == 0 : print(diff)
    else : print(diff+1)