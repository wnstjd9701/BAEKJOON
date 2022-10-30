# 백준 9375번 문제 - 패션왕 신해빈
from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    s = []
    for j in range(n):
        a, b = input().split()
        s.append(b)
    result = Counter(s)
    num = 1
    for key, value in result.items():
        num *= value + 1
    print(num-1)