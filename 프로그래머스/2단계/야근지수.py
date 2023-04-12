# 프로그래머스 2단계 - 야근 지수
import heapq

def solution(n, works):
    answer = 0
    heap = []
    
    # 시간안에 작업을 끝낼 수 있는 경우
    if sum(works) <= n: 
        return answer

    for work in works:
        # 최대 힙
        heapq.heappush(heap, (-work, work)) 
    
    while n > 0:
        work = heapq.heappop(heap)[1] - 1
        heapq.heappush(heap, (-work, work))
        n -= 1
    for h in heap:
        if h[1] < 0:
            continue
        answer += h[1] ** 2
    return answer

print(solution(1,[2,1,2]))