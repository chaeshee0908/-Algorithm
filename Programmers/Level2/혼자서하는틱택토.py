'''
<풀이방법>
불가능한 경우를 따져 0을 리턴해주고 그 외는 모두 가능한 경우이기 때문에 1을 리턴해준다.
불가능한 경우1: O가 선공인데 X가 O보다 더 많은 경우
불가능한 경우2: O가 X보다 2개 이상 많은 경우
불가능한 경우3: 승부가 났지만 경기를 계속 이어간 경우
불가능한 경우3-1: O와 X가 모두 승리한 경우
불가능한 경우3-2: O가 이겼지만 X가 경기를 이어간 경우
불가능한 경우3-3: X가 이겼지만 O가 경기를 이어간 경우
위의 경우에 포함되지 않을 경우는 모두 가능한 경우이다.
'''

def is_finished(arr):
    row = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]]
    column = [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
    diagonal = [[(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]

    # 가로, 세로, 대각선 중 같은 값이 3개 이상일 때 (= 승부가 났을 때)
    for direction in (row, column, diagonal):
        for a in direction:
            cnt = 0
            for i in arr:
                if i in a:
                    cnt += 1
            if cnt == 3:
                return True
            
    return False

def solution(board):
    O = []
    X = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                O.append((i, j))
            elif board[i][j] == 'X':
                X.append((i, j))
    O_num = len(O)  # O의 개수
    X_num = len(X)  # X의 개수
    
    # 불가능한 상황1: O가 선공인데 X가 O보다 더 많은 경우
    if O_num < X_num:
        return 0
    # 불가능한 상황2: O가 X보다 2개 이상 많은 경우
    if O_num - X_num > 1:
        return 0
    # 불가능한 상황3: O나 X가 연달아 3개 있어 승부가 났지만 추가로 놓은 경우
    # O와 X중 하나가 3개 이상일 때 
    if O_num >= 3 or X_num >= 3:
        # O와 X가 모두 승리한 경우
        if is_finished(O) and is_finished(X):
            return 0
        if is_finished(O):
            # O가 이겼지만 X가 경기를 이어간 경우
            if O_num == X_num:
                return 0
        if is_finished(X):
            # X가 이겼지만 O가 경기를 이어간 경우
            if O_num > X_num:
                return 0  
            
    return 1

board1 = ["O.X", ".O.", "..X"]
board2 = ["OOO", "...", "XXX"]
board3 = ["...", ".X.", "..."]	
board4 = ["...", "...", "..."]

print(solution(board4))