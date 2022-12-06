# 백준 1743번 문제 - 음식물 피하기
from collections import deque
dx, dy = [0,0,-1,1], [1,-1,0,0]
n, m, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    global cnt
    cnt = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))
    return cnt
res = []
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = 0
            res.append(bfs(i,j))
print(max(res))
