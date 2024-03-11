MOD = 1000000007

def find_best_team(abilities):
    n = len(abilities)
    dp = [0] * n
    dp[0] = abilities[0]

    for i in range(1, n):
        dp[i] = max(dp[i-1] + abilities[i], abilities[i])
        if i >= 2:
            dp[i] = max(dp[i], dp[i-2] + abilities[i])
        if i >= 3:
            dp[i] = max(dp[i], dp[i-3] + abilities[i-1])

    team_sum = sum(dp) % MOD
    return team_sum


T = int(input())  

for case in range(1, T+1):
    N = int(input())  
    abilities = list(map(int, input().split()))  

    best_team_sum = find_best_team(abilities)
    print(f"#{case} {best_team_sum}")
