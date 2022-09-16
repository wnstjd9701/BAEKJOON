# 백준 10845번 문제 - 큐
import collections 
import sys

N = int(sys.stdin.readline())
queue = collections.deque()

for i in range(N):
    q = sys.stdin.readline().split()
    if q[0] == 'push':
        queue.append(int(q[1]))
    elif q[0] == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif q[0] == 'size':
        print(len(queue))
    elif q[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif q[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif q[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
# END
