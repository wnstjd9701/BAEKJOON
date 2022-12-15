# 백준 16234번 문제 - 인구 이동
from collections import deque
dx, dy = [0,0,-1,1], [1,-1,0,0]
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    union_country = []
    union_country.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    union_country.append((nx, ny))
    return union_country
    
while True:
    visited = [[False]*n for _ in range(n)]
    move = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                union_country = bfs(i, j)
                if 1 < len(union_country):
                    move = True
                    population = sum([graph[x][y] for x, y in union_country]) // len(union_country)
                    for x, y in union_country:
                        graph[x][y] = population
    
    if not move:
        break
    else:
        answer += 1

print(answer)