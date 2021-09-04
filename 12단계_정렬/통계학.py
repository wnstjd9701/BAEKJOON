# 백준 2108번 문제 - 통계학
n = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
arr.sort()
print(sum(arr) // len(arr)) # 산술평균
print(arr[n // 2]) # 중앙값

print()