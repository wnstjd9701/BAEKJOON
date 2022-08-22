# 프로그래머스 1단계 - 같은 숫자는 싫어
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer

