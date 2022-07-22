#d(n) : n과 n의 각 자리수를 더하는 함수
#ex) d(75) = 75 + 7 + 5 = 87
MAX = 10001
d = [-1] * MAX
def self_number(x) :
    if x < 10 :
        return x * 2
    ret = x
    for j in str(x) :
        ret += int(j)
    return ret

for i in range(1,MAX) :
    if d[i] == -1 :
        print(i)
    temp = self_number(i)
    if temp < MAX :
        d[temp] = 1