# 백준 14888번 문제 - 연산자 끼워넣기
n = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split());
max_result = - int(1e9)
min_result = int(1e9)

def dfs(add, sub, mul, div, sum_value, idx):
    global max_result, min_result
    if idx == n:
        max_result = max(max_result, sum_value)
        min_result = min(min_result, sum_value)
        return
    if add:
        dfs(add-1, sub, mul, div, sum_value + number[idx], idx + 1)
    if sub:
        dfs(add, sub-1, mul, div, sum_value - number[idx], idx + 1)
    if mul:
        dfs(add, sub, mul-1, div, sum_value * number[idx], idx + 1)
    if div:
        dfs(add, sub, mul, div-1, int(sum_value / number[idx]), idx + 1)
        
dfs(add, sub, mul, div, number[0], 1)
print(max_result)
print(min_result)