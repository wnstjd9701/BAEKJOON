# 프로그래머스 2단계 - 2017 팁스타운 - 예상 대진표
def solutino(n,a,b):
    cnt = 0
    while a != b:
        a = (a//2) + (a%2)
        b = (b//2) + (b%2)
        cnt += 1
    return cnt