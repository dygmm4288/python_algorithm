import sys
readline = sys.stdin.readline

n = int(readline())
soldier = list(map(int,readline().split()))
if n == 1 :
    print('권병장님, 중대장님이 찾으십니다')
    sys.exit(0)
effective_range = list(map(int,readline().split()))

max_length = effective_range[0]

for i in range(1,n-1) :
    if soldier[i] <= max_length :
        max_length = max(max_length,soldier[i] + effective_range[i]) 
if max_length >= soldier[-1] :
    print('권병장님, 중대장님이 찾으십니다')
else :
    print('엄마 나 전역 늦어질 것 같아')