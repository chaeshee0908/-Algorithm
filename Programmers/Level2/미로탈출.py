'''
<풀이방법>
bfs를 이용하여 최단거리를 구한다. 
S -> L -> E의 경로가 최단 거리가 되도록 해야하므로 각각 [S -> L의 최단 거리] + [L -> E의 최단거리]의 값을 구해주어야한다. 
이때 둘 중 하나라도 가지 못한다면 -1을 리턴한다. 
distance로 각 위치의 최단거리를 저장해준다.

주의할 점: maps의 가로, 세로가 같지 않을 수도 있으므로 런타임 에러에 주의해야한다. 
'''

from collections import deque
INF = int(1e9)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start, end, distance, maps):
    q = deque([])
    n = len(distance)
    m = len(distance[0])
    x, y = start
    ex, ey = end
    distance[x][y] = 0
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and distance[nx][ny] == INF:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

    return distance[ex][ey]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    maps = [list(s) for s in maps]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)

    result = 0
    for v in (start, lever):
        distance = [[INF] * m for _ in range(n)]
        if v == start:
            end = lever
        else:
            end = exit 
        result += bfs(v, end, distance, maps)
    
    if result >= INF:
        return -1
    else:
        return result


maps1 = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
maps2 = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]

print(solution(maps1))