# 골드4 1504번 
# https://www.acmicpc.net/problem/1504

'''
<풀이 방법> 
두 가지 경우 가능 (1->v1->v2->N) / (1->v2->v1->N)
두 가지 경우에 따른 최단경로 구해준다 
1->v1, v1->v2, v2->N의 각각의 최단 경로를 구해주고 최단경로들의 합을 비교하여 더 짧은 경로를 반환
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

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
            cost = next_dist + now_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

# 두 가지 경우 가능 (1->v1->v2->N) / (1->v2->v1->N)
method = [[1, v1, v2, N], [1, v2, v1, N]]
calc = 0
result = INF
while calc < 2:
    dist = 0
    for i in range(3):
        distance = [INF] * (N + 1)
        dijkstra(method[calc][i])
        dist += distance[method[calc][i+1]]
    result = min(result, dist)
    calc += 1

if result >= INF:
    print(-1)
else:
    print(result)
        
    
    