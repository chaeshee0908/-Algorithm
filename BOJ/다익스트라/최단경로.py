# 골드4 1753번
# https://www.acmicpc.net/problem/1753

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (V + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        now_dist, now = heapq.heappop(q)
        # 이미 최단 경로 저장된 경우 패스
        if now_dist > distance[now]:
            continue
        for i in graph[now]:
            next, next_dist = i
            cost = now_dist + next_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] >= INF:
        print('INF')
    else:
        print(distance[i])