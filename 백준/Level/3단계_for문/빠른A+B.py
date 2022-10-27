# 백준 15552번 문제 - 빠른 A+B
import sys

T = int(input())
for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
