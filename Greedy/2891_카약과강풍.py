# 경기는 5분 안에 시작해야 하는 상황
# 자신의 바로 다음이나 전에 경기하는 팀에게만 카약을 빌려주려고 한다
# 다른 팀에게서 받은 카약은 또 다른 팀에게 빌려줄 수 없다
# 카약을 적절히 빌렸을 때, 출발하지 못하는 팀의 최솟값은 몇 팀인가
import sys 
readline = sys.stdin.readline

n,s,r = map(int,readline().split())

damaged = list(map(int,readline().split()))
spare = list(map(int,readline().split()))

teams = [1] *(n+1) 
teams[0] = 0

for team_number in damaged :
    teams[team_number] -= 1
for team_number in spare :
    teams[team_number] += 1

for i in range(1,n+1) :
    if teams[i] == 0 :
        if teams[i-1] > 1 :
            teams[i-1] -= 1
            teams[i] += 1
        elif i + 1 <= n and teams[i+1] > 1 :
            teams[i+1] -= 1
            teams[i] += 1

print(len(list(filter(lambda x : x == 0,teams)))-1)
