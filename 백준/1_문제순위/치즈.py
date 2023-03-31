# 백준 2636번 문제 - 치즈
from collections import deque
dx, dy = [0,0,-1,1], [1,-1,0,0]
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    visited = [[0]*m for _ in range(n)]
    
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    visited[nx][ny] = 1
    cheese.append(cnt)
    return cnt

cheese = []        
time = 0
while True:
    time += 1
    cnt = bfs()
    
    if cnt == 0:
        break
print(time-1)
print(cheese[-2])