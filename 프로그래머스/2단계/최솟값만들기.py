# 프로그래머스 2단계 - 최솟값 만들기
def solution(A,B):
    answer = 0
    A.sort() # 오름차순
    B.sort(reverse=True) # 내림차순
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer

