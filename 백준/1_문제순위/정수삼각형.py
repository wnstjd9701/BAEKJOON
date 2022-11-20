# 백준 1932번 문제 - 정수 삼각형
n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))
for i in range(len(dp)):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[-1]))