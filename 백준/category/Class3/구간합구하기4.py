# 백준 11659번 문제 - 구간 합 구하기
import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, input().split()))

sum_list = [0]
total = 0
for i in range(len(arr)):
    total += arr[i]
    sum_list.append(total)
for _ in range(m):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i-1])
    