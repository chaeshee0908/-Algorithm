# 실버4 11399번
# https://www.acmicpc.net/problem/11399

N = int(input())
minutes = list(map(int, input().split()))

minutes.sort(reverse=True)
result = 0
for i in range(N):
    result += (i+1) * minutes[i]

print(result)