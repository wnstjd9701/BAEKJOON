# 백준 1676번 문제 - 팩토리얼 0의 개수
from math import factorial
n = int(input())
num = list(str(factorial(n)))
cnt = 0
stack = []
for i in range(len(num)-1,0, -1):
    if num[i] == '0':
        cnt += 1
    else: 
        break
print(cnt)