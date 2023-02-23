from collections import deque

n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
l = int(input())
turn = []
for _ in range(l):
    t, d = map(str, input().split())
    turn.append((int(t), d))
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d, x, y = 0, 0, 0
time, i = 0, 0
queue = deque()
queue.append((x, y))
while 1:
    x = x + dx[d]
    y = y + dy[d]
    time += 1
    if x < 0 or x >= n or y < 0 or y >= n or (x, y) in queue:
        break
    queue.append((x, y))
    if graph[x][y] == 0:
        queue.popleft()
    else:
        graph[x][y] = 0
        
    if time == turn[i][0]:
        if turn[i][1] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        if i + 1 < len(turn):
            i += 1

print(time)