# 백준 2606번 문제 - 바이러스
n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0]*(n+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
dfs(1)
print(sum(visited)-1)