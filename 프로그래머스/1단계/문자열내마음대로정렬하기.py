# 프로그래머스 1단계 - 문자열 내 마음대로 정렬하기
def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))

print(solution(["abce", "abcd", "cdx"], 2))
print(solution(["sun", "bed", "car"], 1))