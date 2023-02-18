# 실버5 1316번
# https://www.acmicpc.net/problem/1316

N = int(input())
words = []
for _ in range(N):
    words.append(input())

cnt = 0
for word in words:
    spell = [word[0]]

    for i in range(1, len(word)):
        if word[i] != spell[-1]:
            spell.append(word[i])
    
    for i in range(len(spell)):
        # 떨어져 나간 단어가 있는 경우
        if spell.count(spell[i]) > 1:
            break
        # 모두 확인했을 때 떨어져 나간 단어가 없는 그룹 단어인 경우
        if i == len(spell) - 1:
            cnt += 1

print(cnt)