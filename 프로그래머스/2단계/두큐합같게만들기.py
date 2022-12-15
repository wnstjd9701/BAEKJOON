# 프로그래머스 2단계 - 두 큐 합 같게 만들기
from collections import deque
def solution(queue1,queue2):
    answer = 0
    queue1 = deque((queue1))
    queue2 = deque((queue2))
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    limit = len(queue1) * 3
    if (sum_q1 + sum_q2) % 2 != 0:
        return -1
    
    while True:
        if sum_q1 > sum_q2:
            v = queue1.popleft()
            queue2.append(v)
            sum_q1 -= v
            sum_q2 += v
            answer += 1
        elif sum_q1 < sum_q2:
            v = queue2.popleft()
            queue1.append(v)
            sum_q1 += v
            sum_q2 -= v
            answer += 1
        else: 
            break
        if answer == limit:
            answer = -1
            break
        
    return answer

print(solution([1, 2, 1, 2],[1, 10, 1, 2]))