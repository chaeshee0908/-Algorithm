# 골드4 2665번
# https://www.acmicpc.net/problem/2665

'''
<풀이방법>
우선순위 큐는 최소힙을 보장하므로 최소 힙 사용을 위해 검은 방을 1, 흰 방을 0으로 바꾸어 흰 방을 우선적으로 방문하도록 한다.
changes는 원하는 지점까지 검은 방을 흰 방으로 변경할 최소 개수로 지정한다. 값을 넣기 전 무한으로 초기화해준다. 
검은 방 -> 흰 방 변경 개수는 [기존 방 변경 개수]와 [이전 칸까지의 방 변경 개수 + 이전 칸 검은 방 유무(1 또는 0)]중 작은 값이다.
정점 사이의 거리를 검정 방의 유무로 변경하면 기존 다익스트라 알고리즘대로 수월하게 풀 수 있다.
'''

import heapq
INF = int(1e9)

n = int(input())
rooms = []
for _ in range(n):
    rooms.append(list(map(int, list(input()))))

# 최소 힙을 사용하기 위해 흰 방과 검은 방 변경
for i in range(n):
    for j in range(n):
        if rooms[i][j] == 0:
            rooms[i][j] = 1
        else:
            rooms[i][j] = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))    # 검은 방 유무(검은 방일 떄 1), x, y
    changes[0][0] = 0
    while q:
        black, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and changes[nx][ny] > black + changes[x][y]:
                changes[nx][ny] = black + changes[x][y]
                heapq.heappush(q, (rooms[nx][ny], nx, ny))

# 도달하기 까지 검정 방을 바꿔야하는 가장 작은 수
changes = [[INF] * n for _ in range(n)]
dijkstra()

print(changes[n-1][n-1])