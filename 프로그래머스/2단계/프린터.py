# 프로그래머스 2단계 - 프린터
def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for v,i in enumerate(priorities)])
    print(d)
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

solution([1, 1, 9, 1, 1, 1], 5)