# 프로그래머스 2단계 - H-Index
def solution(citations):
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx 
print(solution([3,0,6,1,5]))