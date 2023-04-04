# 백준 11650번 문제 - 좌표 정렬하기
n = int(input())
coord = []

for i in range(n):
    x, y = map(int, input().split())
    coord.append([x,y])
coord.sort(key = lambda x: (x[0], x[1]))
for i in coord:
    print(i[0], i[1])