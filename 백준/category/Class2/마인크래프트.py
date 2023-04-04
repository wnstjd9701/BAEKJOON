# 백준 18111번 문제 - 마인크래프트
n, m, b = map(int, input().split())
inventory = [1 for _ in range(b)]
land = [[0]*(m) for _ in range(n)]
time = 0
height = 0
for i in range(n):
    land[i] = list(map(int, input().split()))
