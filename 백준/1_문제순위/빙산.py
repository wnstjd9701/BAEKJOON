# 백준 2573번 문제 - 빙산
from collections import deque
dx, dy = [0,0,-1,1], [1,-1,0,0]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

year = 0
while True:
    visited = [[0]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                res += bfs(i,j)
               
    # 빙산 깎기
    for i in range(n):
        for j in range(m):
            if graph[i][j] > count[i][j]:
                graph[i][j] -= count[i][j]
            else:
                graph[i][j] = 0

    if res >= 2:
        break
    if res == 0:
        year = 0
        break
    year += 1

print(year)