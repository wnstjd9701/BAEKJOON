# 백준 16236번 문제 - 아기 상어
from collections import deque
dx, dy = [0,0,-1,1], [1,-1,0,0]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
