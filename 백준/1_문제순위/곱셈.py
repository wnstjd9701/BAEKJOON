# 백준 1629번 문제 - 곱셈
a, b, c = map(int, input().split())
# 1. b의 값이 짝수인지 홀수인지 파악
# 2. b의 값이 짝수라면 10^10 -> (10^5)^2 형태로 바꿔준다
# 3. b의 값이 홀수라면 10^11 -> (10^5)^2 * 10 형태로 바꿔준다.
def power(a, b):
    if b==1: # b의 값이 1
        return a % c
    else:
        temp = power(a, b//2)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c
print(power(a,b))