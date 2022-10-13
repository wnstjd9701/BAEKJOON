# 프로그래머스 2단계 - 다음 큰 숫자
def solution(n):
    c = n+1
    while True:
        if bin(c).count('1') == bin(n).count('1'):
            return c
        c += 1