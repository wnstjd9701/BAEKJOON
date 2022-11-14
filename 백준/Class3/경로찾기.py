# 백준 11403번 문제 - 경로 찾기
# DFS
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]

def dfs(x):
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)
    return visited
for i in range(n):
    visited = [0 for _ in range(n)]
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

# BFS
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def bfs(x):
    queue = deque([x])
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1

for i in range(n):
    bfs(i)
for i in visited:
    print(*i)

# 플로이드 워셜 알고리즘
import sys
input = sys.stdin.readline

N = int(input().rstrip())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

for k in range(0, N):         # 경유지 노드
    for i in range(0, N):     # 출발 노드
        for j in range(0, N): # 도착 노드
            if matrix[i][k]==1 and matrix[k][j]==1:
                matrix[i][j] = 1


for m in matrix:
    print(*m)