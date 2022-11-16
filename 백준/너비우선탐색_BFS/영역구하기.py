# 백준 2583번 문제 - 영역 구하기
from collections import deque
dx, dy = [0,0,-1,1], [1,-1,0,0]
m, n, k = map(int, input().split())
graph = [[0]*(n) for _ in range(m)]
for _ in range(k):
    x, y, x1, y1 = map(int, input().split())
    for i in range(y, y1):
        for j in range(x, x1):
            graph[i][j] = 1

area = 1
res = []
def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 1
    area = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안에 있고 그래프가 1이고 방문을 하지 않았다면 
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx,ny))
                area += 1
    return area
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0: 
            res.append(bfs(i,j))
print(len(res))
res.sort()
for i in res:
    print(i, end=' ')