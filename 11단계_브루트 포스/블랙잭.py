# 백준 2798번 문제 - 블랙잭
n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0 
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] > m:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])
print(result)
