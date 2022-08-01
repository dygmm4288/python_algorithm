import sys
readline = sys.stdin.readline
from functools import cmp_to_key

k,n = map(int,readline().split())

numbers = []
MAX_VALUE = ''
# 여러번 넣을 수는
# 길이가 더 길거나
# 길이가 같다면 더 큰 수
for _ in range(k) :
    item = readline().strip()
    if (len(item) > len(MAX_VALUE) or
        (len(item) == len(MAX_VALUE) and
        int(item) > int(MAX_VALUE))
       ):
         MAX_VALUE = item
    numbers.append(item)

for _ in range(n-k) :
    numbers.append(MAX_VALUE)

def compare(a,b) :
    aplusb = a + b
    bplusa = b + a
    return int(bplusa) - int(aplusb)
#정렬이 관건인데
numbers.sort(key=cmp_to_key(compare))
print(''.join(map(str,numbers)))
  
