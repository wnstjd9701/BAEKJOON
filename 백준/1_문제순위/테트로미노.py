# 백준 14500번 문제 - 테트로미노
import sys
input = sys.stdin.readline

def dfs(x, y, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if idx == 1:
                    visit[nx][ny] = 1
                    dfs(x, y, idx + 1, total + arr[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                dfs(nx, ny, idx + 1, total + arr[nx][ny])
                visit[nx][ny] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [([0] * m) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for x in range(n):
    for y in range(m):
        visit[x][y] = 1
        dfs(x, y, 0, arr[x][y])
        visit[x][y] = 0

print(ans)