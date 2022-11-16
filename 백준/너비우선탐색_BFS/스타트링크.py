# 백준 5014번 문제 - 스타트링크
from collections import deque
from sys import stdin  # importing certain function instead of whole module is better
# there must be 2 blank lines beetwen imports and rest of your script

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
# you should separate functions and other code with 2 blank lines

my_input = stdin.readline  # you should separate built-in input function and your "custom" one by naming it other way
f, s, g, u, d = map(int, my_input().split())
visited = [0 for _ in range(f+1)]  # you can use _ in your cycles to prevent cycle variable use extra memory
count = [0 for _ in range(f+1)]  # same as previous code string
print(bfs(s))
