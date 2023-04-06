# 프로그래머스 2단계 - 연속 부분 수열 합의 개수
def solution(elements):
    result = set()
    elements_length = len(elements)
    elements = elements * 2
    
    for i in range(elements_length):
        for j in range(elements_length):
            result.add(sum(elements[j:j+i+1]))
    return len(result)
            
print(solution([7,9,1,1,4]))