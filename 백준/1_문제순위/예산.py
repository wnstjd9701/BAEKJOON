# 백준 2512번 문제 - 예산
n = int(input())
money = list(map(int, input().split()))
budget = int(input())
start, end = 0, max(money)

def binary(money):
    start = 0
    end = max(money)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in money:
            if i >= mid:
                cnt += mid
            else:
                cnt += i

        if cnt <= budget:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary(money))
