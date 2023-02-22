# 실버2 1260번
# https://www.acmicpc.net/problem/1260

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    # 양방향
    graph[a].append(b)
    graph[b].append(a)

# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것 먼저
for i, g in enumerate(graph):
    graph[i] = sorted(g)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)  