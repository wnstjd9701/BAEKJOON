# 프로그래머스 1단계 - 3진법 뒤집기
def solution(n):
    answer = 0
    nums = []
    
    while n >= 1:
        nums.append(n%3)
        n = n//3
    nums = nums[::-1]
    for i in range(len(nums)):
        answer += nums[i] * (3**i)
    
    return answer

n = int(input())
print(solution(n))