# 백준 10610번 문제 - 30
n = list(input())

answer = -1
if min(n) == '0':
    max_num = sorted(n, reverse=True)
    max_num = int(''.join(max_num))

    if max_num % 3 == 0:
        answer = max_num

print(answer)