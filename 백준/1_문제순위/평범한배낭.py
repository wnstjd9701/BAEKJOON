# 백준 12865번 문제 - 평범한 배낭
n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
weight = []
value = []

for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

for i in range(1, n+1): # 물건 idx
    for j in range(1, k+1): # 가방의 무게
        if j < weight[i-1]: # [이전물건][같은무게]
            dp[i][j] = dp[i-1][j]
        else: # max(
            # 현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게],
            # knapsack[이전 물건][현재 가방 무게])
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]] + value[i-1])

print(dp[n][k])