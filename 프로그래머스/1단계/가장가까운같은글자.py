# 프로그래머스 1단계 - 가장 가까운 같은 글자
def solution(s):
    answer = []
    d = dict()
    for i in range(len(s)):
        if s[i] not in d:
            answer.append(-1)
        else:
            answer.append(i-d[s[i]])        
        d[s[i]] = i
    return answer
print(solution("banana"))