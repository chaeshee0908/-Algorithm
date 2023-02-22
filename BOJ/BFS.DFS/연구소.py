# 골드4 14502번
# https://www.acmicpc.net/problem/14502

'''
풀이 방법: 가능한 3곳에 모든 경우의 수로 벽을 세우고(완전탐색) 모든 경우 때 바이러스가 퍼지는 수를 계산하여(bfs) 가장 안전구역이 많은 경우 찾아내기
'''

n, m = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

numbers = [i for i in range(8)]
from itertools import combinations, product
from collections import deque
import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(q):
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                q.append((nx, ny))
    return cnt

virus = []
wall_num = 0
# 처음 바이러스 위치, 처음 벽 개수
for i in range(n):
    for j in range(m):
        if room[i][j] == 2:
            virus.append((i, j))
        elif room[i][j] == 1:
            wall_num += 1
            
total_virus = 100
position = list(product(numbers, repeat=2))
# 벽 3개 세워보기
for comb in combinations(position, 3):
    lab = copy.deepcopy(room)
    wall = 0
    for c in comb:
        x, y = c
        # 범위 안에 들어오고 빈 칸이어야함
        if 0 <= x < n and 0 <= y < m and lab[x][y] == 0:
            lab[x][y] = 1   # 벽으로 변경
            wall += 1
    # 벽이 3개 세워지지 않은 경우 패스
    if wall != 3:
        continue
    q = deque()
    for v in virus:
        q.append(v)
    cnt = bfs(q)
    total_virus = min(total_virus, cnt)

print(n*m - (wall_num + 3 + total_virus))           
          