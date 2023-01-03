# 백준 1068번 문제 - 트리
n = int(input())
node = list(map(int, input().split()))
m = int(input())
cnt = 0

def dfs(n, node):
    node[n] = -2
    for i in range(len(node)):
        if n == node[i]:
            dfs(i, node)

dfs(m, node)
print(node)
for i in range(len(node)):
    if node[i] != -2 and i not in node:
        cnt += 1
print(cnt)


