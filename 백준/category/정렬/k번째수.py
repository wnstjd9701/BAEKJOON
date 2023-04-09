# 백준 11004번 문제 - K번째 수
import sys 
input = sys.stdin.readline
n, k = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
print(a[k-1])