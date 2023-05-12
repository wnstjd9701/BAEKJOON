# 백준 13219번 문제 - trains
from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = 1e9

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
ay, ax, by, bx = map(int, input().split())
ax -= 1
ay -= 1
bx -= 1
by -= 1

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[INF for _ in range(n)] for _ in range(n)]
q = []
heappush(q, (graph[ax][ay], ax, ay))
visited[ax][ay] = graph[ax][ay]

while q:
    cost, x, y = heappop(q)

    if graph[x][y] == -1:
        break

    if cost > visited[x][y]:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] != -1:
                next_cost = cost + graph[nx][ny]

                if visited[nx][ny] > next_cost:
                    visited[nx][ny] = next_cost
                    heappush(q, (next_cost, nx, ny))

if visited[bx][by] == INF:
    print(-1)
else:
    print(visited[bx][by])