# 실버2 1012번
# https://www.acmicpc.net/problem/1012

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(field, x, y):
    q = deque([(x, y)])
    field[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
                field[nx][ny] = 0
                q.append((nx, ny))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                bfs(field, i, j)
                cnt += 1
    print(cnt)

