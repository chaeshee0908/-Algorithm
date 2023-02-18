# 실버5 7568번
# https://www.acmicpc.net/problem/7568

N = int(input())
sizes = []
for _ in range(N):
    sizes.append(tuple(map(int, input().split())))

rank = [1] * N
for idx, size in enumerate(sizes):
    my_w, my_h = size
    for s in sizes:
        # 같은 사람이면 패스
        if s == size:
            continue
        w, h = s
        # 상대방이 나보다 덩치 크면 순위 1 낮아짐
        if w > my_w and h > my_h:
            rank[idx] += 1

for r in rank:
    print(r, end=" ")