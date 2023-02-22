# 실버3 2606번
# https://www.acmicpc.net/problem/2606

n = int(input())
t = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(t):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

from collections import deque

def bfs(start):
    visited[start] = True
    q = deque([start])
    virus = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                virus += 1
                q.append(i)
    return virus

print(bfs(1))
    