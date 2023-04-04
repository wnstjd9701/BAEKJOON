# 백준 1927번 문제 - 최소 힙
import heapq
import sys
n = int(sys.stdin.readline())
heap = []
heapq.heapify(heap)
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)
