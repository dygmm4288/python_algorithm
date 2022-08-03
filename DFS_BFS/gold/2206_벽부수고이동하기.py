import sys
readline = sys.stdin.readline
from collections import deque

n,m = map(int,readline().split())
board = [list(map(int,readline().strip())) for _ in range(n)]
dist = [[[0,0] for _ in range(m)] for _ in range(n)]

def bfs() :
    q = deque([[0,0,0]])
    dist[0][0][0] = 1
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    while q :
        y,x,z = q.popleft()
        if y == n -1 and x == m - 1 :
            return dist[y][x][z]
        for i in range(4) :
            ny = dy[i] + y
            nx = dx[i] + x
            if ny >= 0 and ny < n and nx >=0 and nx < m :
                if board[ny][nx] == 0 and dist[ny][nx][z] == 0 :
                    dist[ny][nx][z] = dist[y][x][z] + 1
                    q.append([ny,nx,z])
                elif board[ny][nx] == 1 and z == 0 :
                    dist[ny][nx][z+1] = dist[y][x][z] + 1
                    q.append([ny,nx,z+1])
    return -1
print(bfs())