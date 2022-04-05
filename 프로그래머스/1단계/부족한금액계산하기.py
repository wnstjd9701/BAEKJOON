# 프로그래머스 1단계 - 부족한 금액 계산하기
def solution(price, money, count):
    answer = 0
    total = 0
    for i in range(1, count+1):
        total += price * i
        if total > money:
            return total - money

    return answer