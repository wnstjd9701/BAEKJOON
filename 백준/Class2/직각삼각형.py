# 백준 4153번 문제 - 직각삼각형
while True:
    l = list(map(int, input().split()))
    l.sort()
    if l[0] == 0 and l[1] == 0 and l[2] == 0:
        break
    if l[0]**2 + l[1]**2 == l[2]**2:
        print('right')
    else:
        print('wrong')
