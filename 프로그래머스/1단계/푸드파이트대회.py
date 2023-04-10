# 프로그래머스 1단계 - 푸드 파이트 대회
def solution(food):
    answer = ''
    res = ''
    for i in range(1, len(food)):
        if food[i] >= 2:
            res += (food[i]//2)*str(i)
    answer = res + str(0) + res[::-1] 
    return answer

print(solution([1,3,4,6]))