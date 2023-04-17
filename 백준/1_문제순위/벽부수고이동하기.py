# 백준 2206번 문제 - 벽 부수고 이동하기
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(x, y):
    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited[x][y][0] = 1
    queue = deque()
    queue.append((x, y, 0))
    while queue:
        x, y, wall = queue.popleft()
        if (x, y) == (n-1, m-1):
            return visited[x][y][wall]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and wall == 0 and not visited[nx][ny][1]:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][0] + 1
                elif graph[nx][ny] == 0 and not visited[nx][ny][wall]:
                    queue.append((nx, ny, wall))
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
    return 0

result = bfs(0, 0)
if result:
    print(result)
else:
    print(-1)