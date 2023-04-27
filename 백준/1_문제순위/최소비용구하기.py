# 백준 1916번 문제 - 최소비용 구하기
import sys
import heapq
input = sys.stdin.readline
n, m= int(input()), int(input())
graph = [[] for _ in range(n+1)]
INF = 1e9
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)
print(distance[end])