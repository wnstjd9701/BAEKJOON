# 백준 11722번 문제 - 가장 긴 감소하는 부분수열
n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(1, i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
