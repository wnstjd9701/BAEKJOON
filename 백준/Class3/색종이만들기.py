# 백준 2630번 문제 - 색종이 만들기
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [0,0]
def dfs(x,y,n):
    visited = graph[x][y]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == visited:
                dfs(x,y,n)
                answer[1] += 1
            else:
                answer[0] += 1
dfs(0,0,n)