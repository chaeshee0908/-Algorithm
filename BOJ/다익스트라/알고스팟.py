# 골드4 1261번
# https://www.acmicpc.net/problem/1261

'''
<풀이방법>
우선순위 큐에서 벽의 유무를 1, 0으로 따져 벽이 없는 0일 때 우선순위가 되도록 한다
distance는 원하는 지점까지 벽을 부셔야할 최소 개수로 지정한다. 값을 넣기 전 무한으로 초기화해준다. 
이동할 칸의 벽을 부셔야할 개수는 [기존 벽을 부셔야할 개수]와 [이전 칸까지의 벽을 부셔야할 개수 + 이전칸  벽의 유무(1 또는 0)] 중 작은 값이다.
정점 사이의 거리를 벽의 유무로 변경하면 기존 다익스트라 알고리즘대로 수월하게 풀 수 있다.
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

M, N = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, list(input().rstrip()))))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))    # 벽 유무, x, y
    distance[0][0] = 0
    while q:
        wall, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] > wall + distance[x][y]:
                distance[nx][ny] = wall + distance[x][y]
                heapq.heappush(q, (maze[nx][ny], nx, ny))
                

# 도달하기까지 벽을 부셔야할 최소 개수
distance = [[INF] * M for _ in range(N)]

dijkstra()
print(distance[N-1][M-1])