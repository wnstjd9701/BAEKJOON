# 백준 7785번 문제 - 회사에 있는 사람
n = int(input())
d = dict()
for _ in range(n):
    name, status = map(str, input().split())
    if status == 'enter':
        d[name] = status
    else:
        d[name] = 'leave'
people = []
for key, value in d.items():
    if value == 'enter':
        people.append(key)
people.sort(reverse=True)
for name in people:
    print(name)
    