# 골드4 9663번
# https://www.acmicpc.net/problem/9663

'''
<풀이방법>
row의 index를 세로 위치, value를 가로 위치로 사용한다. 
queen이 서로 존재하려면 같은 행, 열, 대각선 상에 위치하면 안 된다.
n-queens를 세로 한 칸씩 내려가며 확인해본다. 
pypy로 가능
'''

N = int(input())
row = [0] * N

def is_success(x):
    for i in range(x):  # 세로 줄
        # 같은 가로줄 혹은 대각선상에 위치할 때 
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True

def n_queens(x):
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):   # 세로 
        # [x, i]에 퀸을 놓는다
        row[x] = i
        if is_success(x):    # queen을 놓을 수 있는 자리이면
            n_queens(x+1)

cnt = 0
n_queens(0)

print(cnt)