# 백준 15650번 문제 - N 과 M (2)
from itertools import combinations

N, M = map(int, input().split())

p = combinations(range(1, N+1), M)
for i in p:
    print(*i)