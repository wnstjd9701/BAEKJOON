# 백준 14681번 문제 - 사분면 고르기
X = int(input())
Y = int(input())

if X>0 and Y>0:
    print("1")
elif X<0 and Y>0:
    print("2")
elif X<0 and Y<0:
    print("3")
else:
    print("4")