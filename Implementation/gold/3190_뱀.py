import sys,collections
readline = sys.stdin.readline

n = int(readline())
k =int(readline()) 
board = [[0] * n for _ in range(n)]

for _ in range(k) :
    y,x = map(int,readline().split())
    board[y-1][x-1] = 1

l = int(readline())
l_li = collections.deque()
for _ in range(l) :
    l_li.append(list(readline().rstrip().split()))


cur_y,cur_x = 0,0
cur_dir = 1
dy = [-1,0,1,0]
dx= [0,1,0,-1]
ret = 1
# 벽을 만난다면 게임 오버
def in_range(y,x) : 
    return y>=0 and y < n and x >=0 and x < n
# 자기 자신을 만나는지는 어떻게 알지?
q = collections.deque()
while True :
    # 앞으로 전진
    q.append([cur_y,cur_x])
    cur_y += dy[cur_dir]
    cur_x += dx[cur_dir]
    # 벽에 부딪히거나 내 몸에 부딪힌다면
    if not in_range(cur_y,cur_x) or [cur_y,cur_x] in q:
        break
    # 움직였는데 앞에 사과가 있다?
    if board[cur_y][cur_x] == 1 :
        #사과를 없애고 #꼬리는 없애지 않는다
        board[cur_y][cur_x] = 0
    elif board[cur_y][cur_x] == 0 :
        # 꼬리가 따라와야지..
        q.popleft()
    ret += 1
    # 다음번에 방향을 전환해야 한다면
    if l_li and int(l_li[0][0])+1 == ret :
        cmd = l_li.popleft()       
        if cmd[1] == 'D' :
            cur_dir = (cur_dir + 1) % 4
        elif cmd[1] == 'L' :
            cur_dir = (cur_dir+3) % 4
print(ret)


