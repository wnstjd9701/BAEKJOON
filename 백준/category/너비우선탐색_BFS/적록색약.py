# 백준 10026번 문제 - 적록색약
# BFS
from collections import deque
dx, dy = [0,0,-1,1], [1,-1,0,0]
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(str, input())))
answer = 0

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

# 적록색맹이 아닌 사람
visited = [[0]*(n) for _ in range(n)]
answer1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            answer1 += 1
            

# 적록색맹인 사람
visited = [[0]*(n) for _ in range(n)]
answer2 = 0 
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            answer2 += 1
print(answer1, answer2)


# DFS
from collections import deque
import sys
sys.setrecursionlimit(1000000)
dx, dy = [0,0,-1,1], [1,-1,0,0]
n = int(input())
graph = [list(map(str, input())) for _ in range(n)]

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
            dfs(nx,ny)
# 적록색맹이 아닌 경우
visited = [[0]*(n) for _ in range(n)]
answer1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            answer1 += 1

# 적록색맹인 경우
visited = [[0]*(n) for _ in range(n)]
answer2 = 0 
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            answer2 += 1
            dfs(i,j)
print(answer1, answer2)