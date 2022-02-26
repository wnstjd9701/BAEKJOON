# 프로그래머스 1단계 - 최대공약수와 최소공배수
from math import gcd
def lcm(a,b):
  return (a * b) // gcd(a,b)

def solution(a, b):
    c = gcd(a,b)
    d = lcm(a,b)
    answer = [c,d]

    return answer

print(solution(2,5))
