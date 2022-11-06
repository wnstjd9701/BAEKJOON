# 백준 11279번 문제 - 최대 힙
import sys
import heapq

n= int(input())
heap = []
for _ in range(n) :
    x = int(sys.stdin.readline())
    if x :
        heapq.heappush(heap, (-x, x))
    else :
        if len(heap) >= 1 :
            print(heapq.heappop(heap)[1])
        else :
            print(0)