# 백준 9019번 - DSLR
from collections import deque
t = int(input())

def order(num ,case):
    if case == 'D':
        return (int(num)*2) % 10000
    elif case == 'S':
        return (int(num)-1) % 10000
    elif case == 'L':
        tmp = num // 1000
        return num % 1000 * 10 + tmp
    elif case == 'R':
        tmp = num % 10
        return num // 10 + 1000 * tmp

d = ['D','S','L','R']

def bfs(a,b,visited):
    q = deque([[a,'']])
    visited[a] = 1
    while q:
        num, case = q.popleft()
        print(num)
        print(case)
        if num == b:
            print(case)
            break
        for i in range(4):
            n_case = order(num, d[i])
            if visited[n_case] == 0:
                q.append((n_case,case+d[i]))
                visited[n_case] = 1

for _ in range(t):
    visited = [0 for _ in range(10000)]
    a,b = map(int, input().split())
    bfs(a,b,visited)