# 백준 1712번 문제 - 손익분기점
A, B, C = map(int, input().split())
count = 0 
num = int(A / (C-B))
print(num+1)