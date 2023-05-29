# 백준 15903번 문제 - 카드 합체 놀이 
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)
for i in range(m):
    value = heapq.heappop(cards) + heapq.heappop(cards)
    for _ in range(2):
        heapq.heappush(cards, value)
answer = 0 
while cards:
    answer += heapq.heappop(cards)
print(answer)