import sys
readline = sys.stdin.readline
 
n,m,k = map(int,readline().split())

participant = []

for genre in range(m):
    inputs = readline().strip().split()
    for i in range(0,len(inputs),2) :
        participant_index = int(inputs[i])
        participant_score = float(inputs[i+1])
        participant.append((participant_index,participant_score))

participant.sort(key=lambda info:info[1],reverse=True)
final = [False] * (n+1)
#[index,score]
ret = 0
for parti in participant :
    if final[parti[0]] == False and k > 0:
        final[parti[0]] = True
        k -= 1
        ret += parti[1]
print(round(ret,1))

