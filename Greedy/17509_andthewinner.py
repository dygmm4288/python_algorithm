import sys
readline = sys.stdin.readline

problems = []
for i in range(11):
    problems.append(list(map(int,readline().split())))

problems.sort(key=lambda x: x[0])
p_sum = [problems[0][0]]
ret = 0
penality = 0
for i in range(len(problems)) :
    if i == 0 :
        ret += problems[i][0]
    else :
        p_sum.append(p_sum[i-1] + problems[i][0])
        ret += p_sum[i]
    penality += 20 * problems[i][1]
print(ret + penality)
        