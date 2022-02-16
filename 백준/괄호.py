# 백준 9012번 문제 - 괄호
n = int(input())
# '('을 확인하면 stack에 쌓고 ')'을 확인하면 stack에서 pop한다.
for _ in range(n):
    vps = list(input())
    stack = list()
    is_empty = False
    for i in range(len(vps)):
        if vps[i] == '(':
            stack.append(vps[i])
        else:
            if not stack:
                is_empty = True
                break
            else:
                stack.pop()
    if not stack and not is_empty: # 스택이 비어 있고 is_empty가 False
        print('YES')
    else:
        print('NO')