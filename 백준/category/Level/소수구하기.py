# 백준 1929번 문제 - 소수 구하기 
m, n = map(int, input().split()) # m 이상 n 이하 소수 모두 구하기
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num%i == 0:
                return False
        return True

for i in range(m, n+1):
    if isPrime(i):
        print(i)

