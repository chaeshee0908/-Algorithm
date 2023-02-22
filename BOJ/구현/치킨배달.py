# 골드 5 15686번
# https://www.acmicpc.net/problem/15686

from itertools import combinations

N, M = map(int, input().split())
city = []
for _ in range(N):
    line = list(map(int, input().split()))
    city.append(line)

chicken_shop = []
home = []
result = 1e9
# 치킨집, 집 위치 찾기
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken_shop.append((i, j))
        if city[i][j] == 1:
            home.append((i, j))

# 치킨집 치킨거리의 합, 위치 정보
dist_chicken = []
for c in combinations(chicken_shop, M):
    distance = 0    # 도시의 치킨 거리
    for h in home:
        i, j = h
        dist_home = 999 # 각 집에서의 치킨거리
        for k in range(M):
            dist_home = min(dist_home, abs(c[k][0]-i) + abs(c[k][1]-j))
        distance += dist_home
    result = min(result, distance)

print(result)