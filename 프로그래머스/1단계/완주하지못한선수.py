# # 프로그래머스 1단계 - 완주하지 못한 선수
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c: # 정렬 했을 때 participant와 completion이 다를 경우
            return p
    return participant.pop()

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
