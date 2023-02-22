# 골드3 2206번
# https://www.acmicpc.net/problem/2206

'''
풀이 방법: 
visited를 3차원 배열로 하여 벽을 뚫은 경우, 벽을 뚫지 않은 경우의 방문을 확인해준다
벽을 뚫었을 떄의 2차원 배열, 벽을 뚫지 않았을 때의 2차원 배열(지도)를 따로 생각해준다

모든 벽을 한 번씩 뚫어서 확인하는 경우는 시간초과된다 
'''

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, list(input()))))

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque([(0, 0, 1)])
    visited[0][0][1] = 1    # 벽을 하나 부술 수 있는 상태로 시작
    while q:
        x, y, wall = q.popleft()
        if x == n-1 and y == m-1:
            return visited[n-1][m-1][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 만났고 벽을 한 번 부술 수 있는 상태
                if board[nx][ny] == 1 and wall == 1:
                    visited[nx][ny][0] = visited[x][y][wall] + 1
                    q.append((nx, ny, 0))
                # 빈 칸을 만났고 방문한 적 없는 상태
                if board[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))
    return -1

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] 
print(bfs())