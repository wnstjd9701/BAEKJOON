# 백준 11725번 문제 - 트리의 부모찾기
from collections import deque
n = int(input())
tree = [[] for _ in range(n+1)]
dict = {}
for _ in range(n-1):
    root, child = map(int ,input().split())
    tree[root].append(child)
    tree[child].append(root)
for i in range(1, n+1):
    dict[i].append(tree[i])
print(dict)