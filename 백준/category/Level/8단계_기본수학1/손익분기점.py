# 백준 1712번 문제 - 손익분기점
A, B, C = map(int, input().split())
if B>=C: # 0 일 경우
    print(-1)
else:   # 그 외의 경우
    num = int(A / (C-B))
    print(num+1)