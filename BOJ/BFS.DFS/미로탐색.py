# 실버1 2178번
# https://www.acmicpc.net/problem/2178

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, list(input()))))

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 내에 있는지 확인
            if 0 <= nx < N and 0 <= ny < M:
                # 첫 방문인 경우 최단거리 조정
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    q.append((nx, ny))
    return maze[N-1][M-1]

print(bfs(0, 0))