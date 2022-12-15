# 백준 24445번 문제 - 알고리즘 수업 - 너비 우선 탐색 2
from collections import deque
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(n):
    global count
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        v = q.popleft()
        graph[v].sort(reverse=True)
        for i in graph[v]:
            if not visited[i]:
                count += 1
                visited[i] = count
                q.append(i)
bfs(r)
for v in visited[1:]:
    print(v)
