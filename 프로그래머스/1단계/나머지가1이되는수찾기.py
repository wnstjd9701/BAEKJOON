# 프로그래머스 1단계 - 나머지가 1이 되는 수 찾기
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 1:
            return i
