# 실버1 1931번
# https://www.acmicpc.net/problem/1931

N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    # 회의시간, 시작시간, 끝나는시간
    meetings.append([start, end])


result = 0
# 끝나는 시간 1순위, 시작 시간 2순위
meetings = sorted(meetings, key=lambda x: x[0])
meetings = sorted(meetings, key=lambda x: x[1])
# 이전 회의 끝나는 시간
last = 0
for i in range(N):
    meeting = meetings[i]
    start, end = meeting[0], meeting[1]
    # 이전 회의 끝났을 때
    if start >= last:
        result += 1
        last = end

print(result)