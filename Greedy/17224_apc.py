import sys 
stdin = sys.stdin.readline
N, L, K = map(int,stdin().split())

def solved_problem(problems,K,L,solved,value,sub) :
  idx = 0
  ret = 0
  while K > 0 and idx < len(problems) :
      if problems[idx][sub] <= L and not solved[idx] :
          ret += value
          K -= 1
          solved[idx] = True
      elif problems[idx][sub] > L : break
      idx += 1
  return ret


solved = [False] * N
origin_problem = []

for _ in range(N) :
        origin_problem.append(list(map(int,stdin().split())))

copy_problem = origin_problem[:]
# origin_problem sorted by sub1(easy)
origin_problem.sort(key=lambda x : x[0])
# copy_problem sorted by sub2(hard)
copy_problem.sort(key=lambda x : x[1])
ret = 0

ret += solved_problem(copy_problem,K,L,solved,140,1)
ret += solved_problem(origin_problem,K - (ret//140),L,solved,100,0)

print(ret)