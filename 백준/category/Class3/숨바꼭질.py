# 백준 1697번 문제 - 숨바꼭질
from collections import deque
n, k = map(int, input().split())

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v == k:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)

visited = [0 for _ in range(100001)]
print(bfs(n))
