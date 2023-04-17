# 프로그래머스 2단계 - 더 맵게
import heapq
def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < k:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
        
        if len(scoville) == 1 and scoville[0] < k:
            return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))