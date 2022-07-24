import sys
readline = sys.stdin.readline

# G개의 게이트 
# P개의 비행기가 순서대로 도착 예정
# i번째 비행기를 1번부터 gi번째 게이트 중 하나에 영구적으로 도킹
# 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다
# 최대 몇 대를 도킹 시킬 수 있는지?
g = int(readline())
p = int(readline())
planes = [int(readline()) for _ in range(p)]
airport = [i for i in range(g+1)]
def find(a) :
    if a == airport[a] : return a
    airport[a] = find(airport[a])
    return airport[a]
def union(a,b) :
    a = find(a)
    b = find(b)
    if a == b : return;
    airport[a] = b
ret = 0
# gi가 안되면 gi-i번째에 도킹
for plane in planes :
    finding = find(plane)
    if finding == 0 :
        break
    union(finding,finding-1)
    ret += 1
print(ret)
        


