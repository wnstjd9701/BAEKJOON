# 프로그래머스 2단계 - H-Index
def solution(citations):
    citations.sort()
    length = len(citations)

    for i in range(length):
        if citations[i] >= length-i:
            return length-i
    return 0

print(solution([3,0,6,1,5]))