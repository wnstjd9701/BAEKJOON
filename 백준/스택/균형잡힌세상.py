# 백준 4949번 문제 - 균형잡힌 세상
bracket = ['(','[',')',']']
while True:
    stack = []
    string = input()
    if string == '.':
        break
    for s in string:
        if s in bracket: # 괄호가 있을 경우
            if len(stack) == 0:
                stack.append(s)
                continue
            if s == ')' and stack[-1] == '(':
                stack.pop()
                continue
            elif s == ']' and stack[-1] == '[':
                stack.pop()
                continue
            stack.append(s)
    if len(stack):
        print('no')
    else:
        print('yes')
        