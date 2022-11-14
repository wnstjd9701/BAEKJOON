# 백준 6064번 문제 - 카잉 달력
t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    answer = -1
    while x <= m*n:
        if (x-y) % n == 0:
            answer = x
            break
        x += m
    print(answer)
