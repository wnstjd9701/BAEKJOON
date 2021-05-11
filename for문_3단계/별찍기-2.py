# 백준 2439번 문제 - 별찍기 - 2
a=int(input())
for i in range(1,a+1):
    print(" "*(a-i) + "*"*i)