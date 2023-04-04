# 백준 16928번 문제 - 뱀과 사다리 게임
from collections import deque
n, m = map(int, input().split())
board = [0] * 101
visited = [False] * 101

ladder = dict()
snake = dict()
for _ in range(n):
    x,y = map(int, input().split())
    ladder[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

q = deque([1])

while q:
    x = q.popleft()

    if x == 100:
        print(board[x])
        break
    for dice in range(1,7):
        location_next = x + dice
        if location_next <= 100 and not visited[location_next]:
            if location_next in ladder.keys():
                location_next = ladder[location_next]
            if location_next in snake.keys():
                location_next = snake[location_next]
            if not visited[location_next]:
                visited[location_next] = True
                board[location_next] = board[x] + 1
                q.append(location_next)