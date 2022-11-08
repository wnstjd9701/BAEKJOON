# 백준 2468번 문제 - 안전 영역
from collections import deque
n = int(input())
graph = []
dx, dy = [0,0,-1,1],[1,-1,0,0]
graph = [list(map(int, input().split())) for _ in range(n)]
# 2 <= n 행 <= 100 
# 1 <= i 높이 <= 100
# i = 2 ~ max(graph) - 1

# 1 부터 그래프의 (최대 높이-1)까지 확인하기 위해
max_height = []
for i in range(len(graph)):
    max_height.append(max(graph[i]))
max_height = max(max_height)

count = 0

def bfs(x, y, k):
    count = 1
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1 # 방문 처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > k and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    count += 1
                    visited[nx][ny] = 1          
    return count
res = 0
for k in range(max_height + 1):
    visited = [[0]*n for _ in range(n)]
    res_cnt = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and visited[i][j] == 0:
                res_cnt.append(bfs(i,j,k))
                count = 0
    res = max(res, len(res_cnt))
print(res)


    



