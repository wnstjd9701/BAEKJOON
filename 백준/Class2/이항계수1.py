# 백준 11050번 문제 - 이항 계수 1
import sys
import math
n, k = map(int, input().split())
answer = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
print(answer)