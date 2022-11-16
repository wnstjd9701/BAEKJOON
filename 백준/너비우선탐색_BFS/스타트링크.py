# 백준 5014번 문제 - 스타트링크
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == g:
            return count[g]
        for i in (v+u, v-d):
            if 0 < i <= f and not visited[i]:
                visited[i] = 1
                count[i] = count[v] + 1
                q.append(i)
    if count[g] == 0:
        return 'use the stairs'

f, s, g, u, d = map(int, input().split())
visited = [0 for i in range(f+1)]
count = [0 for i in range(f+1)]
print(bfs(s))