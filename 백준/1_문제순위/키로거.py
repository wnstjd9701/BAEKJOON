# 백준 5397번 문제 - 키로거
n = int(input())
l = []
for _ in range(n):
    l.append(list(input()))
for i in range(n):
    stack_l = []
    stack_r = []
    for cmd in l[i]:
        if cmd == '<':
            if stack_l:
                stack_r.append(stack_l.pop())
        elif cmd == '>':
            if stack_r:
                stack_l.append(stack_r.pop())
        elif cmd == '-':
            if stack_l:
                stack_l.pop()
        else:
            stack_l.append(cmd)
    print(''.join(stack_l + list(reversed(stack_r))))