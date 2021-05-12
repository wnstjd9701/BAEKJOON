# 백준 2908번 문제 - 상수
a, b = list(map(str, input().split()))

a = int(a[::-1]) # 역순 배열
b = int(b[::-1])

if a>b:
    print(a)
else :
    print(b)
    