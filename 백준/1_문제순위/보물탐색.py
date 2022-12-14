# 백준 2589번 문제 -보물 탐색
from collections import deque
n, m = map(int, input().split())
dx, dy = [0,0,-1,1], [1,-1,0,0]
graph = [list(map(str, input())) for _ in range(n)]
def bfs(x,y):
    q = deque()
    q.append((x, y))
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
                q.append((nx, ny))
    return cnt - 1
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            # 가장자리가 아님
            if i>0 and i+1<n:
                if graph[i-1][j] == "L" and graph[i+1][j] == "L":
                    continue
            if j>0 and j+1<m:
                if graph[i][j-1] == "L" and graph[i][j+1] == "L":
                    continue
            result = max(result, bfs(i,j))
print(result)