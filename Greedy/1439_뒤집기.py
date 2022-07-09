S = list(map(int,input()))
cnt = [0,0]
prev = S[0]
for cur in S[1:]:
  if cur == prev:
    continue
  elif cur != prev:
    cnt[prev] += 1
    prev = cur
cnt[prev] += 1
print(min(cnt))