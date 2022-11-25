# 백준 2156번 문제 - 포도주 시식
n = int(input())
dp = [0]*10002
grape = [0]*10002
for i in range(1, n+1):
    grape[i] = int(input())

dp[1] = grape[1]
dp[2] = grape[1] + grape[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-3] + grape[i-1] + grape[i], dp[i-2] + grape[i])
print(dp[n])