# N, M, K를 공백으로 구분하여 입력받기
n,m,k = map(int,input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))


def solution(n,m,k,list):
  list.sort()
  list.reverse()
  return list[0] * (m //k) * k + list[1] * (m % k)
  

print(solution(n,m,k,data))

def solution2(n,m,k,list):
  list.sort()
  list.reverse()

  first = list[0]
  second = list[1]

  count = int(m / (k+1) ) * k
  count += m % (k + 1)

  result = 0
  result += (count) * first
  result += (m - count) * second

  print(result)

solution2(n,m,k,data)