# 백준 10866번 문제 - 덱
import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_back':
        d.append(cmd[1])
    elif cmd[0] == 'push_front':
        d.appendleft(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(d):
            n = d.popleft()
            print(n)
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if len(d):
            n = d.pop()
            print(n)
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(d))
    elif cmd[0] == 'empty':
        if len(d):
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if len(d):
            print(d[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(d):
            print(d[-1])
        else:
            print(-1)