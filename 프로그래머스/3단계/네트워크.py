# 프로그래머스 3단계 - 네트워크
from collections import deque
def bfs(graph, visited, n):
    if visited[n] == 1:
        return 0
    q = deque()
    q.append((n))
    visited[n] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                q.append((i))
    return 1
def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i].append(j)
    for i in range(len(graph)):
        answer += bfs(graph, visited, i)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))