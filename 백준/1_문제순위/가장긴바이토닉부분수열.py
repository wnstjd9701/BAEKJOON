# 백준 11054번 문제 - 가장 긴 바이토닉 부분 수열
n = int(input())
arr = list(map(int, input().split()))

dp_increase = [1] * (n)
dp_decrease = [1] * (n)
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp_increase[i] <= dp_increase[j]:
            dp_increase[i] = dp_increase[j] + 1
for i in range(n-1, -1, -1):
    for j in range(i, n):
        if arr[i] > arr[j] and dp_decrease[i] <= dp_decrease[j]:
            dp_decrease[i] = dp_decrease[j] + 1

for i in range(n):
    dp_increase[i] = dp_increase[i] + dp_decrease[i] - 1
print(max(dp_increase))