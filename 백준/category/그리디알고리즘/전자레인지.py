# 백준 10162번 문제 - 전자레인지
import sys
n = int(sys.stdin.readline().rstrip())

buttons = [300, 60, 10]
count = [0] * 3
if(n % 10 != 0):
    print(-1)
else:
    for i in range(3):
        count[i] = n // buttons[i]
        n = n % buttons[i]
    print(count[0], count[1], count[2])

