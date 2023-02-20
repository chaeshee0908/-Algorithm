# 실버5 11866번
# https://www.acmicpc.net/problem/11866

N, K = map(int, input().split())
numbers = [i for i in range(1, N+1)]

result = []
idx = 0
for _ in range(N):
    idx += K-1
    if idx >= len(numbers):
        idx = idx % len(numbers)
    result.append(str(numbers.pop(idx)))

print("<{}>".format(", ".join(result)))   
