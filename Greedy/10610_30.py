N = list(input())

if not "0" in N:
  print(-1)

else :
  sum = 0
  for i in map(int,N):
    sum += i
  if sum % 3 != 0:
    print(-1)
  else :
    N.sort(reverse=True)
    print(''.join(N))

