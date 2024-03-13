# 1249. [S/W 문제해결 응용] 4일차 - 보급로
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y):
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if dist[x][y] + graph[nx][ny] < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + graph[nx][ny]
                    q.append((nx, ny))

for test_case in range(1, int(input())+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    dist = [[1e9]*N for _ in range(N)]
    dist[0][0] = graph[0][0]

    bfs(0,0)
    print("#{} {}".format(test_case, dist[N-1][N-1]))