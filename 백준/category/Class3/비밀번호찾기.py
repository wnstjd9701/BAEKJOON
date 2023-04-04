# 백준 17219번 문제 - 비밀번호 찾기
import sys
n, m = map(int, sys.stdin.readline().strip().split())
dict = {}

for _ in range(n):
    key, value = sys.stdin.readline().strip().split()
    dict[key] = value 
for _ in range(m):
    print(dict[sys.stdin.readline().rstrip()])

