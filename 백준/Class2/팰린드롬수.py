# 백준 1259번 문제 - 팰린드롬 수
while True:
    n = input()
    if int(n) == 0:
        break
    p = n[::-1]
    if p == n:
        print('yes')
    else: 
        print('no')