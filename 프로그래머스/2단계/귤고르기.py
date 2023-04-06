# 프로그래머스 2단계 - 귤 고르기
from collections import Counter
def solution(k, tangerine):
    answer = 0
    d = sorted(Counter(tangerine).items(), reverse = True, key = lambda x : x[1])
    for key, value in d:
        if k <= 0:
            break
        k -= value
        answer += 1
    return answer
print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))