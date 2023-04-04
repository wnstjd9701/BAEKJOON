# 백준 2467번 문제 - 용액
import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

left_idx = 0
right_idx = n - 1

ans = abs(liquids[left_idx] + liquids[right_idx])
ans_left = left_idx
ans_right = right_idx

while left_idx < right_idx: # left_idx와 right_idx는 만나면 안된다
    tmp = liquids[left_idx] + liquids[right_idx]

    if abs(tmp) < ans:
        ans_left = left_idx
        ans_right = right_idx
        ans = abs(tmp)

        if ans == 0:
            break
    
    if tmp < 0:
        left_idx += 1
    
    else:
        right_idx -= 1

print(liquids[ans_left], liquids[ans_right])

# Binary Search
import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

ans = float("INF")
ans_left = 0
ans_right = 0

for i in range(n-1):
    current = liquids[i]

    start = i + 1
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        tmp = current + liquids[mid]

        if abs(tmp) < ans:
            ans = abs(tmp)
            ans_left = i
            ans_right = mid

            if tmp == 0:
                break
        
        if tmp < 0:
            start = mid + 1
        
        else:
            end = mid - 1

print(liquids[ans_left], liquids[ans_right])