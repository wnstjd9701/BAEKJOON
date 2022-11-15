# 백준 18352번 문제 - 특정 거리의 도시 찾기
from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [False for _ in range(n+1)]
dist = [0 for _ in range(n+1)]
answer = []
def dfs(x):
    queue = deque([x])
    visited[x] = True
    while queue:
        now = queue.popleft()
        
        for i in graph[now]:
            if visited[i] == False:
                dist[i] = dist[now] + 1
                visited[i] = True
                queue.append(i)
                if dist[i] == k:
                    answer.append(i)
dfs(x)
if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)