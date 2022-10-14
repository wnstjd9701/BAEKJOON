# 프로그래머스 2단계 - 월간 코드 챌린지 시즌2 - 괄호 회전하기
from collections import deque
def check(s):
    answer = 0
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
    return 1 if len(stack) == 0 else 0
def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s): answer += 1
        s = s[1:] + s[:1]
    print(answer)
    return answer

solution("[](){}")