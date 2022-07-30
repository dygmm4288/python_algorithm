import sys
readline = sys.stdin.readline

#모든 값이 0으로 채워져 있는 길이가 n인 배열 a가 있다.
# 1. 배열에 있는 값 하나를 1 증가시킨다
# 2. 배열에 있는 모든 값을 두 배 시킨다

# 배열 B가 주어졌을 떄, 배열 A를 B로 만들기 위한 연산의 최소 횧수
n = int(readline())
B = list(map(int,readline().split()))
A = [0] * n
ret = 0
def is_even(li) :
    for item in li :
        if item % 2 != 0 :
            return False
    return True
def big_odd(li) :
    big = [-1,-1]
    for i,item in enumerate(li) :
        if item % 2 == 0 : continue
        if big[0] < item :
            big[0] = item
            big[1] = i
    return big[1]
while True :
    if A == B :
        break
    # B가 모두 짝수로 이뤄져 있다
    if is_even(B) :
        B = list(map(lambda x : x // 2,B))
        ret += 1
    # B 중 몇개가 홀수이다
    else :
        B[big_odd(B)]-=1
        ret += 1
    
print(ret)
    