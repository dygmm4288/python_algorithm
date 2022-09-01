N = int(input())
seq = list(map(int,input().split()))
S = int(input())

for i in range(N) :
    if S <= 0 :
        break
    selected = i
    for j in range(i+1,min(N,i+S+1)) :
        if seq[selected] < seq[j] :
            selected = j
    # 더이상 큰 숫자가 없다.. 이미 정렬된 상태이다
    if selected == i :
        continue
    # 움직임
    for j in range(selected,i,-1) :
        seq[j],seq[j-1] = seq[j-1],seq[j]
    S -= (selected-i)
        
print(' '.join(map(str,seq)))
    