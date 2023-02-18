# 실버5 1193번
# https://www.acmicpc.net/problem/1193

X = int(input())

for n in range(5000):
    # n(n+1)//2 이용
    num1 = n * (n+1) // 2
    num2 = (n+1) * (n+2) // 2
    if num1 < X <= num2:
        num = n + 1
        order = X - num1
        break

# 분모와 분자의 합이 짝수일 때 
if (num + 1) % 2 == 0:
    print("{}/{}".format(num + 1 - order, order))
# 분모와 분자의 합이 홀수일 때
else:    
    print("{}/{}".format(order, num + 1 - order))
