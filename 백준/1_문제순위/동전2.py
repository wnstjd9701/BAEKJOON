# 백준 2294번 문제 - 동전 2
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [10001] * (k+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
# print(dp)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])

# DP