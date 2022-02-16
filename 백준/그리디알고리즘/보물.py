# 백준 1026번 문제 - 보물
from os import sep


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
S = 0
for i in range(n):
    S += a[i]*b[i]
print(S)
print(a, sep="")
print(b)