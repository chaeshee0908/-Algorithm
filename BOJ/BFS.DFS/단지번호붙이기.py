# 실버1 2667번
# https://www.acmicpc.net/problem/2667

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, num):
    q = deque([(x, y)])
    board[x][y] = num
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:
                board[nx][ny] = num
                cnt += 1
                q.append((nx, ny))
    return cnt        

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, list(input()))))

num = 1 # 동번호
part = []   # 아파트 단지
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            num += 1
            part.append(bfs(i, j, num))

print(num-1)
part.sort()
for p in part:
    print(p)

