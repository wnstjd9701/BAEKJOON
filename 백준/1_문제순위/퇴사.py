# 백준 14501번 문제 - 퇴사
n = int(input())
profit = [[0,0]]
dp = [0] * 20

for _ in range(n):
    time, price = map(int, input().split())
    profit.append([time, price])

for i in range(1, n+1):
    x = profit[i][0] - 1
    dp[i] = max(dp[i-1], dp[i])
    dp[i+x] = max(dp[i-1] + profit[i][1], dp[i+x])
    print(dp)
print(dp[n])