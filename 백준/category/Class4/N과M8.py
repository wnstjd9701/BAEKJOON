# 백준 15654번 문제 - N과 M (8)
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start, n):
            temp.append(nums[i])
            dfs(i)
            temp.pop()

dfs(0)