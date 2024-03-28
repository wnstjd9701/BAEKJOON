N = int(input())
pwd = list(input())
stack = []
for i in range(len(pwd)):
    if pwd[i] == '#':
        if len(stack) == 0:
            continue
        stack.pop()
    else:
        stack.append(pwd[i])
print(stack)