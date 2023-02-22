# 골드5 7576
# https://www.acmicpc.net/problem/7576

from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(q):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))        


M, N = map(int, input().split())
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))

# 익은 토마토 위치
tomato_start = deque()
# 첫 익은 토마토 찾기
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato_start.append((i, j))
            
bfs(tomato_start)
day = 0
# 걸린 일자 수
for l in box:
    max_value = max(l)
    day = max(day, max_value)
day -= 1
# 모든 토마토가 익지 못한다면 -1
for l in box:
    if 0 in l:
        day = -1

print(day)        
