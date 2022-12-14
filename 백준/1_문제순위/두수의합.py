# 백준 3273번 문제 - 두 수의 합
n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())
answer = 0
left, right = 0, n-1
while left < right:
    temp = a[left] + a[right]
    if temp == x:
        answer += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(answer)