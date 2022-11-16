# 백준 4963번 문제 - 섬의 개수
from collections import deque
dx = [0,0,-1,1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]
def bfs(graph, x, y):
    queue = deque()
    graph[x][y] = 0
    queue.append((x, y))
    global cnt
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 
                queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    graph = []
    if w == 0 and h == 0:
        break
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    result = []
    cnt = 1
    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(graph, i,j)
                answer += 1
    print(answer)