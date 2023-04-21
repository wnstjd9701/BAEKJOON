# 백준 1107번 문제 - 리모컨
import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
cnt = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    
    for i in range(len(nums)):
        if int(nums[i]) in broken:
            break

        elif i == len(nums) - 1:
            cnt = min(cnt, abs(int(nums) - target) + len(nums))

print(cnt)