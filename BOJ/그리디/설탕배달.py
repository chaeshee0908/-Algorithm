# 실버4 2839번
# https://www.acmicpc.net/problem/2839

N = int(input())
cnt = 0

# N이 5로 나눠지지 않으면
while N % 5 != 0 and N > 0:
    N -= 3
    cnt += 1

# N이 5의 배수일 때
if N > 0:
    cnt += N // 5
# N이 5와 3 모두 나눠지지 않을 때
elif N < 0:
    cnt = -1

print(cnt)