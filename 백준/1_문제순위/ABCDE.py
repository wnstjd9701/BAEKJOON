# 백준 13023번 문제 - ABCDE
# dfs
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int , input().split())
visited = [0]*(n)
graph = [ [] for _ in range(n) ]
answer = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start , depth):
    global answer
    visited[start] = 1
    if depth == 4:
        answer = True
        return
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i , depth+1)
    visited[start]=0

for i in range(n):
    dfs(i ,0)
    if answer:
        break
if answer:
    print(1)
else:
    print(0)