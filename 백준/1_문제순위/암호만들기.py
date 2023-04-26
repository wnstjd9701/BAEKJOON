# 백준 1759번 문제 - 암호 만들기
import sys
input = sys.stdin.readline
l, c = map(int, input().split())
words = sorted(list(map(str, input().split())))
answer = []

def back_tracking(cnt, idx):
    if cnt == l:
        vo, co = 0, 0

        for i in range(l):
            if answer[i] in ['a', 'e', 'i', 'o', 'u']:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print("".join(answer))

        return

    for i in range(idx, c):
        answer.append(words[i])
        back_tracking(cnt + 1, i + 1)
        answer.pop()

back_tracking(0, 0)