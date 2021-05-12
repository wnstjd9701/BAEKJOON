# 백준 2588번 문제 - 곱셈
A = int(input())
B = input()

First = A * int(B[2:])
Second = A * int(B[1:2])
Last = A * int(B[0:1])

Mul = First + Second*10 + Last*100
print(First,Second,Last,Mul,sep="\n")