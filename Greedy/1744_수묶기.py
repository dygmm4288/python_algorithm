import sys
readline = sys.stdin.readline

#수열의 최대 합을 구하려면
#2개를 묶은 값이 최대가 되야함
#양수는 양수끼리, 음수는 음수끼리
#2개를 묶은 값은 큰수끼리 묶어야 한다
#1이나 0은 안묶어도 됨 안묶는게 이득

n = int(readline())
pos = []
neg = []
ret = 0
for _ in range(n):
    value = int(readline())
    if value > 1:
        pos.append(value)
    elif value <= 0 :
        neg.append(value)
    else :
        ret += value
pos.sort(reverse=True)
neg.sort()
def for_calc(li) :
    ret = 0
    for i in range(0,len(li),2) :
        ret += li[i] * li[i+1]
    return ret
def calc(li) :
    ret = 0
    if len(li) % 2 == 0 :
        ret += for_calc(li)
    else :
        ret += li.pop() + for_calc(li)
    return ret
ret += calc(pos) + calc(neg)
print(ret)
       