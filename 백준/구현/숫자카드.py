# 백준 10815번 문제 - 숫자 카드
import sys
input = sys.stdin.readline
n = int(input())
arr = set(map(int,input().split()))
m = int(input())
m_arr= list(map(int,input().split()))

for i in range(m):
    if m_arr[i] in arr : 
        print(1,end=' ')
    else : print(0,end=' ')