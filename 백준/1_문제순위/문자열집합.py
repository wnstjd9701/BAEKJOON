# 백준 14425번 문제 - 문자열 집합
# 딕셔너리를 이용한 풀이
n, m = map(int, input().split())
d = dict()
answer = 0
for _ in range(n):
    s = input().split()
    d[s] = 1

for i in range(m):
    t = input().split()
    if t in d:
        answer += 1
print(answer)

n, m = map(int, input().split())
s = []
inspect = []
answer = 0
for _ in range(n):
    s.append(input())
for _ in range(m):
    inspect.append(input())
for i in range(m):
    if inspect[i] in s:
        answer += 1
print(answer)