# 프로그래머스 1단계 - 예산
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)