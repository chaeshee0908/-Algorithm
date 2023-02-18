# 실버5 2941번
# https://www.acmicpc.net/problem/2941

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for c in croatia:
    if c in word:
        word = word.replace(c, 'a')

print(len(word))
