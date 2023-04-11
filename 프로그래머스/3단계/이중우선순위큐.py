# 프로그래머스 3단계 - 이중 우선순위 큐
import heapq
def solution(operations):
    heap = []
    max_heap = []
    
    for o in operations:
        current = o.split()
        if current[0] == 'I':
            num = int(current[1])
            heapq.heappush(heap, num) # 최소 힙
            heapq.heappush(max_heap, (num*-1, num)) # 최대 힙
        else:
            if len(heap) == 0:
                pass
            elif current[1] == '1':
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
            elif current[1] == '-1':
                min_value = heapq.heappop(heap)
                max_heap.remove((min_value*-1, min_value))
    
    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        return [0,0]
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))