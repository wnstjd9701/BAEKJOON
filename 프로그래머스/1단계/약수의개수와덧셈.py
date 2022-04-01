# 프로그래머스 1단계 - 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        print(cnt)
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
    
m, n = map(int, input().split())

print(solution(m, n))