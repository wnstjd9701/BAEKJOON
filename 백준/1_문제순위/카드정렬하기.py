# 백준 1715번 문제 - 카드 정렬하기
import heapq
import sys
input = sys.stdin.readline

n = int(input())
cards = []
result = 0

for i in range(n):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        plus = heapq.heappop(cards) + heapq.heappop(cards)
        result += plus
        heapq.heappush(cards, plus)
    
    print(result)