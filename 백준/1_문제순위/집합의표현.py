# 백준 1717번 문제 - 집합의 표현
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 1:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
    else:
        union_parent(a, b)