# 백준 1011번 문제 - Fly me to the Alpha Centauri
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    cnt = 0
    move = 1
    move_plus = 0 # 이동한 거리의 합
    while move_plus < distance:
        cnt += 1
        move_plus += move 
        if cnt % 2 == 0:
            move += 1
    print(cnt)