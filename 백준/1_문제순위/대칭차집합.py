# 백준 1269번 문제 - 대칭 차집합
a_cnt, b_cnt = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A^B))
print(len((A|B)-(A&B)))