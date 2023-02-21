# 백준 16236번 문제 - 아기 상어
from collections import deque
dx, dy = [0,0,-1,1], [1,-1,0,0]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y, shark_size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j

def eatFish(x, y, shark_size):
    distance = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.(BFS의 특징)
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    temp = []
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    if 0 < graph[nx][ny] < shark_size:
                        temp.append((nx,ny,distance[nx][ny]))
    return sorted(temp,key=lambda x: (-x[2],-x[0],-x[1]))

cnt = 0
result = 0
while True:
    shark = eatFish(x, y, shark_size)
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()

    result += dist

    graph[x][y], graph[nx][ny] = 0,0
    x, y = nx, ny
    cnt += 1
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
print(result)