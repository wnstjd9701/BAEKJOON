# 백준 18111번 문제 - 마인크래프트
import sys
input = sys.stdin.readline
n, m, b = map(int, input().split()) # 세로, 가로, 블록 개수
graph = []
graph.append(list(map(int, input().split())) for _ in range(m))

answer = int(1e9)
g_level = 0

for i in range(257):
    use_block = 0
    take_block = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] > i:
                take_block += graph[x][y] - i
            else:
                use_block += i - graph[x][y]
    
    if use_block > take_block + b:
        continue

    count = take_block * 2 + use_block

    if count <= answer:
        answer = count
        g_level = i

print(answer, g_level)