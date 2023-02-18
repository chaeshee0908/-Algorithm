# 실버4 10773번
# https://www.acmicpc.net/problem/10773

K = int(input())
money = []

for _ in range(K):
    n = int(input())
    if n == 0:
        money.pop()
    else:
        money.append(n)

print(sum(money))