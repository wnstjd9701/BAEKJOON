# 백준 11720번 문제 - 숫자의 합
a = int(input())
b = list(input())
result = 0

for i in b:
    result += int(i)
print(result)
