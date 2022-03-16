# 프로그래머스 1단계 - 두 개 뽑아서 더하기
from itertools import combinations
def solution(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i)) 
    return sorted(answer)
