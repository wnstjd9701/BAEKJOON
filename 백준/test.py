# test python
from collections import deque
dx, dy = [0,0,-1,1], [1,-1,0,0]
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    global cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))
    return cnt
answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 1
            answer.append(bfs(i, j))
answer.sort()
print(len(answer))
for i in answer:
    print(i)