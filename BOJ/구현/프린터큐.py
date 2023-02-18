# 실버3 1966번
# https://www.acmicpc.net/problem/1966

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    # 프린트할 문서 중요도
    i_print = importance[M]
    cnt = 0
    while True:
        max_imp = max(importance)
        # 원하는 문서가 중요도가 제일 높지 않을 떄
        if max_imp > i_print:
            # 가장 중요도 높은 문서들 삭제할 때 까지 
            while max_imp in importance:
                idx = importance.index(max_imp)  # 중요도 가장 높은 문서의 인덱스
                before_len = len(importance)
                left_imp = importance[:idx]
                right_imp = importance[idx+1:]
                importance = right_imp + left_imp
                # 원하는 문서의 인덱스 찾기
                if M > idx:
                    M = M - idx - 1
                else:
                    M = (before_len - 1 - idx) + M
                cnt += 1    # 문서 프린트
        # 원하는 문서가 중요도가 가장 높을 때
        else:
            for i in range(M):
                # 동일한 중요도 문서일 때 
                if importance[i] == i_print:
                    cnt += 1    # 문서 프린트
            cnt += 1    # 원하는 문서 프린트
            break
    print(cnt)
                
