# 백준 2407번 문제 - 조합
import math
n, m = map(int, input().split())

print(int(math.factorial(n) // (math.factorial(m)*math.factorial(n-m))))