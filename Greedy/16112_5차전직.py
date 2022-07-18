# 총 n개의 퀘스트를 진행해서 n개의 아케인 스톤을 받아야 한다
# 각 아케인 스톤에 5억 이상의 경험치를 모으면 5차 전직을 진행할 수 있는 자격이 주어진다
# i번째 퀘스트 진행하면 ai의 경험지와 i번째 아케인 스톤ㄴ이 주어진다
# i번째 퀘스트의 보상 경험치를 받을 때 아케인스톤에도 ai의 경험치가 추가된다

# 최대 경험지 제한을 없앱러ㅣ고, 최대 k개의 아케인 스톤이 동시에 활성화 되어 있을수 있도록 바꿈
# 낮은 경험치를 가진 아케인 스톤을 먼저 활성화 시킨뒤
# 큰 순서대로 퀘스트를 클리어 하면서 경험치의 합을 키운다
# 근데 최대 k개네
import sys
readline = sys.stdin.readline

n,k = map(int,readline().split())
expr = list(map(int,readline().split()))

expr.sort()
active = 0
ret = 0
for i in range(len(expr)) :
    #활성화 되어 있는 아케인 스톤 + 현재 경험치
    ret += active * expr[i]
    #최대 k개 까지 활성화 
    if k > active :
        active += 1
print(ret)

