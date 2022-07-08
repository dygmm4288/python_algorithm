N = int(input())
ret = [0,0,0]
buttons = [300,60,10]
if N % 10 == 0 :
  for i in range(3):
    ret[i] = N // buttons[i]
    N %= buttons[i]
  for r in ret:
    print(r,end=' ')
else :
  print(-1)