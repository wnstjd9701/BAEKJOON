# 백준 11725번 문제 - 트리의 부모찾기
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    root, child = map(int ,input().split())
    tree[root].append(child)
    tree[child].append(root)

visited = [0]*(n+1)

def dfs(v):
    for i in tree[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(visited[x])
