# 골드3 1238
# https://www.acmicpc.net/problem/1238

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        now_dist, now = heapq.heappop(q)
        if now_dist > distance[now]:
            continue
        for i in graph[now]:
            next, next_dist = i
            cost = now_dist + next_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

round_time = 0
distance = [INF] * (n + 1)
dijkstra(x)
way_x_dist = distance
for i in range(1, n + 1):
    # 본인 마을인 경우 패스
    if i == x:
        continue
    distance = [INF] * (n + 1)
    dijkstra(i)
    round_time = max(round_time, way_x_dist[i] + distance[x])

print(round_time)
    
    