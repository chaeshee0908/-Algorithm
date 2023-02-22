# 골드5 10026번
# https://www.acmicpc.net/problem/10026

n = int(input())
paint = []
for _ in range(n):
    paint.append(list(input()))

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque([(x, y)])
    color = paint[x][y]
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and paint[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

p_num = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            p_num += 1

# 적록색약용 그림 변경
for i in range(n):
    for j in range(n):
        if paint[i][j] == 'R':
            paint[i][j] = 'G'

w_num = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            w_num += 1
print(p_num, w_num)
