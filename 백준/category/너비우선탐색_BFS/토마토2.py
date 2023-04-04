# 백준 7569번 문제 - 토마토
from collections import deque
import sys
input = sys.stdin.readline
dx=[0,0,-1,1,0,0] # 높이
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]
m,n,h = map(int, input().split())
graph = []
queue = deque()
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            if temp[j][k] == 1:
                queue.append([i,j,k])
    graph.append(temp)

def bfs():
    while queue:
        x,y,z = queue.popleft()
        # i 가 높이 
        # j 가 n
        # k 가 m
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # nx : 높이를 넘으면 안됨
            # ny : n을 넘으면 안됨
            # nz : m을 넘으면 안됨
            if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append((nx,ny,nz))

bfs()
answer = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))
print(answer - 1)

