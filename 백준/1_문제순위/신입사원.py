# 백준 1946번 문제 - 신입 사원
from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a,b))
    arr.sort(key = lambda x: x[0])

    res = arr[0][1]
    cnt = 1 # 첫번째는 무조건 사원으로 뽑히기 때문에 1부터 시작
    for compare in arr:
        if res > compare[1]:
            cnt += 1
            res = compare[1]
    print(cnt)