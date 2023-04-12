# 프로그래머스 2단계 - k진수에서 소수 개수 구하기
import math
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def k_digit(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n,k)    
        rev_base += str(mod)
    return rev_base[::-1]

def solution(n, k):
    answer = 0
    k_digit_number = k_digit(n,k)
    n_list = k_digit_number.split('0')
    for i in n_list:
        if i != "":
            if isPrime(int(i)):
                answer += 1    
    return answer
print(solution(437674, 3))