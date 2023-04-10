# 프로그래머스 1단계 - 콜라 문제
def solution(a, b, n):
    answer = 0
    while (n>=a):
        empty_bottle = n % a
        n = (n//a) * b
        answer += n
        n+= empty_bottle
                       
    return answer
print(solution(2,1,20))