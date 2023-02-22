# 실버2 11724번
# https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

result = 0
for i in range(1, n+1):
    if not visited[i]:
        result += 1
        dfs(i)
print(result)