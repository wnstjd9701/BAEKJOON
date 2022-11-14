# 백준 2559번 문제 - 수열
import sys
n, k = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))

result = []
result.append(sum(temp[:k]))
for i in range(n-k):
    result.append(result[i] - temp[i] + temp[k+i])
print(max(result))
