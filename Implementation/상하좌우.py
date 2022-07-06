N = int(input())
direction = input().split()

inRange = lambda y,x,n : y >= 0 and y < n and x >= 0 and x > n
dic = {
    'U' : 0,
    'D' : 1,
    'L' : 2,
    'R' : 3
}
dy = [-1,1,0,0]
dx = [0,0,-1,1]
y = 0
x = 0 
for dir in direction:
    nextY = y + dy[dic[dir]]
    nextX = x + dx[dic[dir]]
    if not inRange(nextY,nextX,N) : continue
    y = nextY
    x = nextX

print(y+1,x+1)


# N을 입력받기
N = int(input())
x, y = 1, 1
# input().split() input()으로 입력받은 문자열을 split()을 통해 공백(스페이스, 탭, 엔터 등)으로 기준으로 나눠준다
# 그 값은 리스트 자료형에 들어가게 된다
plans = input().split() 

dx = [-1,1,0,0]
dy = [0,0,-1,1]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            ny = y + dy[i]
            nx = x + dx[i]
    if(ny < 1 or ny < 1 or nx > n or ny > n):
        continue
    x, y = nx, ny

print(x,y)



