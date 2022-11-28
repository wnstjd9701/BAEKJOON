# 백준 2210번 문제 - 숫자판 점프
from collections import deque
dx, dy = [0,0,-1,1], [1,-1,0,0]
graph = [list(map(str, input().split(' '))) for _ in range(5)]

def dfs(x, y, number):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5:
                dfs(nx, ny, number + graph[nx][ny])
result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
print(len(result))

