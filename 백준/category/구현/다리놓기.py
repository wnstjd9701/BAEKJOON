# 백준 1010번 문제 - 다리 놓기
import math
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    nCr = math.factorial(m) // (math.factorial(n) * (math.factorial(m-n)))
    print(nCr)
