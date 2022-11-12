# 백준 1158번 문제 - 요세푸스 문제
from collections import deque
n, k = map(int, input().split())
answer = []
q = deque([i for i in range(1, n+1)])
while q:
    for i in range(k-1):
        num = q.popleft()
        q.append(num)
    answer.append(str(q.popleft()))
answer = ", ".join(answer)
print('<', end='')
print(answer, end='')
print('>')