# 백준 14425번 문제 - 문자열 집합
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