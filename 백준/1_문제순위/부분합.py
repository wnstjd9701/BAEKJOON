# 백준 1806번 문제 - 부분합
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
num = list(map(int, input().split()))
target, left, right = 0, 0, 0
min_length = 1e9


while True:
    # print("left: ", left, " right: ", right)
    if target >= s:
        min_length = min(min_length, right - left) 
        target -= num[left] 
        left += 1 
        
    else:
        if right == n:
            break
        
        target += num[right] 
        right += 1 

if min_length == 1e9:
    print(0)
else:
    print(min_length)