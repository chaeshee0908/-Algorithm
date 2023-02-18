# 실버4 4673번
# https://www.acmicpc.net/problem/4673

selfNumber = [0] * 10001

for i in range(1, 10001):
    n = i
    # d(n) 10001 이전까지 생성
    while n < 10001:
        selfNumber[n] += 1
        newNumber = n
        # d(n) 계산
        while n > 0:
            newNumber += n % 10
            n //= 10
        if newNumber < 10001:
            selfNumber[newNumber] += 1
        n = newNumber

# selfNumber 각 인덱스의 해당 숫자가 한 번만 호출되었을 경우 셀프넘버
for i in range(1, 10001):
    if selfNumber[i] == 1:
        print(i)