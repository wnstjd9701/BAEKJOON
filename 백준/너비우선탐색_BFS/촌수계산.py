# 백준 2644번 문제 - 촌수계산
from collections import deque
n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(x):
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = visited[x] + 1
            dfs(i)
dfs(x)
print(visited[y] if visited[y] > 0 else -1)