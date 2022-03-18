# 백준 7568번 문제 - 덩치
n = int(input())
info = []
for i in range(n):
    w, h = map(int, input().split())
    info.append((w,h))
for i in info:
    rank = 1
    for j in info:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end= ' ')