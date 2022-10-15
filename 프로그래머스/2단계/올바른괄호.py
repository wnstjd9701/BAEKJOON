# 프로그래머스 2단계 - 스택/큐 - 올바른 괄호
def solution(s):
    answer = True
    stack = []
    for t in s:
        if t == '(':
            stack.append(t)
        elif len(stack) and t == ')':
            stack.pop()
        else:
            return False
    return False if len(stack) else True
    # stack