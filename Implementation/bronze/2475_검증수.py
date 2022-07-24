#검증수 : 6번째 자리에 들어가고 고유번호 5자리에 들어간느 5개의 숫자를 가각 제곱한 수의 합을 10으로 나눈 나머지

import sys
readline = sys.stdin.readline

id_number = list(map(int,readline().strip().split()))

print(sum(map(lambda x : x * x,id_number)) % 10)