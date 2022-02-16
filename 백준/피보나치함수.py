# 백준 1003번 문제 - 피보나치 함수
a = int(input())

zero = [1,0,1]
one = [0,1,1]

def fiboNum(n):
    length = len(zero)
    if length <= n:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print("%d %d"%(zero[n],one[n]))

for i in range(a):
    k = int(input())
    fiboNum(k)