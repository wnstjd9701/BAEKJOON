# 백준 11055번 문제 - 가장 큰 증가 부분 수열
n = int(input())
numbers = list(map(int, input().split()))

dp = numbers[:]
dp[0] = numbers[0]

for i in range(1, n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + numbers[i])

print(max(dp))