# 백준 2638번 문제 - 치즈
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0,0,-1,1],[1,-1,0,0]
def bfs():
    q = deque()
    visited = [[0]*m for _ in range(n)]
    q.append((0,0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif graph[nx][ny] == 1: # 치즈일 경우 공기 접촉한 횟수 증가
                    visited[nx][ny] += 1
    melted = []
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                melted.append((i,j))
    return melted

answer = 0
while True:
    melted = bfs()
    if not melted:
        break
    answer += 1
    for x, y in melted:
        graph[x][y] = 0

print(answer)