# 프로그래머스 1단계 - 없는 숫자 더하기
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer


def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]
    answer = 0
    for i in numbers:
        if i in num:
            num.remove(i)    
    answer = sum(num)
    return answer