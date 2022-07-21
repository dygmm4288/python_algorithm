import sys
readline = sys.stdin.readline

toInt = lambda x : 0 if x == 'S' else 1 if x == 'R' else 2
def play(a,b) :
    if a == b :
        return 1
    elif (a+2)%3 == b :
        return 2
    else:
        return 0
r = int(readline())
s = list(map(toInt, readline().strip()))
n = int(readline())
friends = [list(map(toInt,readline().strip())) for _ in range(n)]
    
rounds = []
min_ret = 0
max_ret = 0
# 각 라운드 별로
for i in range(r) :
  # 각 친구와 겨뤘을 때
  temp_max = 0
  for all in range(3) :
    temp = 0
    for j in range(n) :
      temp += play(all,friends[j][i])
    temp_max = max(temp_max,temp)
  max_ret += temp_max
  for j in range(n) :
      min_ret += play(s[i],friends[j][i])
print(min_ret)
print(max_ret)