N = int(input())
peaks = list(map(int,input().split()))
best_peak = peaks[0]
cnt = 0
ret = 0
for next_peak in peaks[1:]:
  if(best_peak < next_peak) :
    best_peak = next_peak
    ret = max(ret,cnt)
    cnt = 0
  else : cnt += 1
ret = max(ret,cnt)
print(ret)
    