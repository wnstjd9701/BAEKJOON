# 수열 조작 - Deque
from collections import deque

n = int(input())
queue = deque()
for i in range(1, n+1):
    queue.append(i)

print(queue)