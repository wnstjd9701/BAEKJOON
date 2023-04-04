# 백준 2805번 문제 - 나무 자르기
import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(trees)


while start <= end:
    mid = (start + end) // 2
    tree = 0 # 잘린 나무 합
    for i in trees:
        if i > mid: # mid 모다 큰 나무 높이는 잘림
            tree += i - mid
    if tree >= m: # 원하는 나무 높이보다 더 많이 잘렸으면
        start = mid + 1
    else:  # 원하는 나무 높이보다 덜 잘렸으면
        end = mid - 1
print(end)
        


