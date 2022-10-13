# 연습문제 - 그리디 - 만들 수 없는 금액
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 떄 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
# End