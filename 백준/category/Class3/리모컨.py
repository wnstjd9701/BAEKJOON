# 백준 1107번 문제 - 리모컨
import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
break_num = list(map(int, input().split()))

# 현재 채널에서 +, -만 사용하는 경우
min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        # 각 숫자의 버튼이 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in break_num:
            break

        # 고장난 숫자 없이 마지막 자리가지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)