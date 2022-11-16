# 백준 7562번 문제 - 나이트의 이동
from collections import deque
import sys
input = sys.stdin.readline
dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]
t = int(input())
def bfs(cur_x, cur_y):
    queue = deque()
    queue.append((cur_x, cur_y))
    while queue:
        x, y = queue.popleft()
        if x == move_x and y == move_y:
            print(graph[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
for _ in range(t):
    l = int(input())
    graph = [[0]*(l) for _ in range(l)]
    cur_x, cur_y = map(int, input().split())
    move_x, move_y = map(int, input().split())
    bfs(cur_x, cur_y)