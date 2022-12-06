# 백준 3184번 문제 - 양
from collections import deque
r, c = map(int, input().split())
graph = [list(map(str, input())) for _ in range(r)]
dx, dy = [0,0,-1,1], [1,-1,0,0]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    global count_sheep, count_wolf

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c: # 범위를 벗어나 탈출을 할 수 있는 경우
                count_wolf = -1
                count_sheep = -1
                break
            elif 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if graph[nx][ny] == '#':
                    visited[nx][ny] = 1
                    continue
                elif graph[nx][ny] == '.':
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif graph[nx][ny] == 'o':
                    count_sheep += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    count_wolf += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    
    return count_sheep, count_wolf

visited = [[0]*c for _ in range(r)]
res = [0,0]
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'v' and not visited[i][j]: # 늑대가 사냥을 시작
            count_sheep = 0
            count_wolf = 1 # 늑대 한마리로 시작
            cnt = bfs(i, j)
            if cnt[1] == -1: # 늑대 혼자 있는 경우 
                continue
            if cnt[0] > cnt[1]: # 양이 늑대보다 많은 경우
                res[0] += cnt[0]
            else: # 늑대가 양보다 많거나 같은 경우
                res[1] += cnt[1]
        elif graph[i][j] == 'o' and not visited[i][j]: # 양이 사냥 시작
            count_sheep = 1 # 양 한마리로 시작
            count_wolf = 0
            cnt = bfs(i, j)
            if cnt[0] == -1: # 양 혼자 있는 경우
                continue
            if cnt[0] > cnt[1]: # 양이 늑대보다 많은 경우
                res[0] += cnt[0]
            else: # 늑대가 양보다 많거나 같은 경우
                res[1] += cnt[1]
for i in res:
    print(i, end=' ')



