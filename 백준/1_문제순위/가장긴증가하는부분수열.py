# 백준 11053번 문제 - 가장 긴 증가하는 부분 수열
n = int(input())  # 수열의 길이
array = list(map(int, input().split()))  # 주어진 수열

# DP 테이블 1로 초기화
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 증가하는 부분 수열의 길이값
print(max(dp))