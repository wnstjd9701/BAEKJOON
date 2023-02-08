# 백준 1303번 문제 - 전쟁-전투
from collections import deque
dx, dy = [0,0,-1,1], [1,-1,0,0]
n, m = map(int, input().split())
graph = [list(input()) for i in range(m)]
visited = [[0]*n for j in range(m)]

def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == color:
                cnt += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
    return cnt**2
white_cnt = 0
blue_cnt = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                white_cnt += bfs(i, j, 'W')
            else:
                blue_cnt += bfs(i, j, 'B')
print(white_cnt, blue_cnt)


