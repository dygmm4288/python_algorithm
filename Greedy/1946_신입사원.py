import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
  N = int(sys.stdin.readline().strip())
  arr = [0] * (N + 1)
  for _ in range(N):
    a, b = map(int,sys.stdin.readline().split())
    arr[a] = b
  ret = 1
  best = arr[1]
  for value in arr[2:]:
    if best > value:
      ret += 1
      best = value
  print(ret)
  