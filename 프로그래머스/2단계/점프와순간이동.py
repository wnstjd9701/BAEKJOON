# 프로그래머스 2단계 - Summer/Winter Coding(~2018) - 점프와 순간이동 
def solution(n):
    ans = 0
    while True:
        if n % 2 != 0:
            n -= 1
            ans += 1
        n = n // 2
        if n == 0:
            return ans