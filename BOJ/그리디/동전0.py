# 실버4 11047번
# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

money = 0
cnt = 0
while K != money:
    coin = coins.pop()
    if K - money >= coin:
        num = (K - money) // coin
        cnt += num
        money += coin * num

print(cnt)