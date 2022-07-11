N = int(input())
alpha = [0] * 26

for _ in range(N):
  value = input()
  for i in range(len(value)):
    digit = pow(10,len(value) - i)
    alpha[ord(value[i]) - ord('A')] += digit

alpha.sort(reverse=True)

cnt = 9
ret = 0
for value in alpha:
  if value :
    ret += (value * cnt)
    cnt -= 1

print(ret // 10)
