# 백준 2164번 문제 - 카드2
from collections import deque
n = int(input())
c = deque()
for i in range(1, n+1):
    c.append(i)
for _ in range(n-1):
    c.popleft()
    c.append(c.popleft())
print(c[0])