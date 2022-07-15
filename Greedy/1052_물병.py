import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())

ret = 0
while True :
  if bin(N).count('1') <= K :
      break
  else :
    N += 1
    ret += 1
print(ret)
    