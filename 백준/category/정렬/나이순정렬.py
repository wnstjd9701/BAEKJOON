# 백준 10814번 문제 - 나이순 정렬
n = int(input())
member = []
for _ in range(n):
    member.append(list(input().split()))
    # [['21', 'Junkyu'], ['21', 'Dohyun'], ['20', 'Sunyoung']]
member.sort(key = lambda x: int(x[0]))
for i in member:
    print(i[0], i[1])

