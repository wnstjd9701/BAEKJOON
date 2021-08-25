# 백준 2869번 문제 - 달팽이는 올라가고 싶다
import sys
import math
a, b, v = map(int, sys.stdin.readline().split());
day = (v-b) / (a-b) # 마지막 날은 미끄러지지 않으므로 v-b
print(math.ceil(day))
