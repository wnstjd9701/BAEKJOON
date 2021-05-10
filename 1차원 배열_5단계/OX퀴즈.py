# 백준 8958번 문제 - OX퀴즈
n = int(input())
for i in range(n):
    ox = input()
    cnt = 0
    sum_ox = 0
    for i in ox:
        if i=='O':
            cnt+=1
        else:
            cnt=0
        sum_ox += cnt
    print(sum_ox)    

