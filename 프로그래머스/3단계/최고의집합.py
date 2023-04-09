# 프로그래머스 3단계 - 최고의 집합
def solution(n, s):
    answer = []
    if s < n: return [-1]
    
    for i in range(n):
        answer.append(s//n)
    idx = len(answer) - 1
    for j in range(s % n):
        answer[idx] += 1
        idx -= 1
    return answer
print(solution(2,9))