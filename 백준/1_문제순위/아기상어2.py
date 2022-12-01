# 백준 17086번 문제 - 아기 상어 2
from collections import deque
dx = [0,0,-1,1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
n, m = map(int, input().split())
graph = [list(map(int, input().split(' '))) for _ in range(n)]
ans = 0 

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                # print('상어', graph[nx][ny])
                # print('거리', visited[x][y])
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if graph[nx][ny] == 1:
                    print(visited)
                    return visited[nx][ny]-1

dist = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 1:
            dist.append(bfs(i, j))

print(max(dist))