# 백준 9935번 문제 - 문자열 폭발
import sys
input = sys.stdin.readline
# 입력값 처리
s = input().rstrip()
bomb = input().rstrip()

# stack으로 문자열 폭발 구현
stack = []
bomb_length = len(bomb)

for char in s:
    stack.append(char)
    # print(stack)
    if char == bomb[-1] and ''.join(stack[-bomb_length:]) == bomb:
        for _ in range(bomb_length):
            stack.pop()

# 결과 출력
if stack:
    print(''.join(stack))
else:
    print('FRULA')