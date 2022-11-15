# 백준 10807번 문제 - 개수 세기
n = int(input())
arr = list(map(int, input().split()))
v = int(input())
print(arr.count(v))
cnt = 0
for i in arr:
    if i == v:
        cnt += 1
print(cnt)
