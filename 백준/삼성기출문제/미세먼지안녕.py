# 백준 17144번 문제 - 미세먼지 안녕!
dx, dy = [0,0,1,-1], [1,-1,0,0]
r, c, t = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    n = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] >= 5:
            bfs(i,j)
