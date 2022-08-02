import sys

readline = sys.stdin.readline

n, m = map(int, readline().split())
board = [list(readline()) for _ in range(n)]
alpha = [0] * 26
A = ord('A')
ret = 0


def dfs(y, x, cnt):
    global ret
    ret = max(ret, cnt)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if (ny >= 0 and ny < n and nx >= 0 and nx < m
                and alpha[ord(board[ny][nx]) - A] == 0):
            alpha[ord(board[ny][nx]) - A] = 1
            dfs(ny, nx, cnt + 1)
            alpha[ord(board[ny][nx]) - A] = 0

alpha[ord(board[0][0]) - A] = 1
dfs(0, 0, 1)
print(ret)
