# 백준 9205번 문제 - 맥주 마시면서 걸어가기
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([home[0], home[1]])
    while q:
        x, y = q.popleft()
        if abs(x-festival[0]) + abs(y-festival[1]) <= 1000: # 거리가 1000이내일 경우
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                new_x, new_y = conv[i]
                if abs(x-new_x) + abs(y-new_y) <= 1000:
                    q.append([new_x, new_y])
                    visited[i] = 1
    print('sad')
    return 
t = int(input())
for _ in range(t):
    n = int(input())
    home = [int(x) for x in input().split()]
    print(home)
    conv = []
    for _ in range(n):
        conv.append(list(map(int, input().split())))
    festival = [int(x) for x in input().split()]
    print(festival)
    visited = [0 for i in range(n+1)]
    bfs()