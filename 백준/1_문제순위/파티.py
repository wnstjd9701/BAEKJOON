# 백준 1238번 문제 - 파티
import heapq
n, m, x = map(int, input().split())
# n: 노드, m: 간선의 개수
# 모든 학생 x에 갈 수 있고 x에서 집으로 돌아올 수 있는 데이터만 입력
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b,cost))

def dijkstra(start):
    q = []
    distance = [1e9] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance
result = 0
for i in range(1,n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])
    
print(result)