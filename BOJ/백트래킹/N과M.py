# 실버3 15649
# https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
recur = 0

def bt(st, recur):
    if recur == m:
        print(' '.join(st))
        return
    for i in range(n):
        s = list(map(int, st))
        if nums[i] in s:
            continue
        bt(st+str(nums[i]), recur+1)

bt('', 0)

    