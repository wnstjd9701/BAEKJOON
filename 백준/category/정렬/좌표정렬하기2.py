# 백준 11651번 문제 - 좌표 정렬하기 2
n = int(input())
coord = []
for _ in range(n):
    x, y = map(int, input().split())
    coord.append([x,y])
coord.sort(key = lambda x: (x[1], x[0]))
for i in coord:
    print(i[0] ,i[1])