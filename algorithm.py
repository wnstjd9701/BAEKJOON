# 파이썬 알고리즘에서 사용 되는 함수 or 로직 모음
from collections import deque

from collections import defaultdict
d = defaultdict(int) # Int형 defaultdict

# 알파벳을 아스키 코드 숫자로 반환 (ord)
num = ord('A') 
a = 'a'
a.isupper() # 대문자인지 확인
a.islower() # 소문자인지 확인


# 에라토스테네스의 체 알고리즘
import math
n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1): # 2부터 n의 제곱근(루트n)까지의 모든 수를 확인
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# n을 k진수로 바꾸기
def k_digit(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n,k)    
        rev_base += str(mod)
    return rev_base[::-1]

# 최단경로 다익스트라 알고리즘
import heapq
import sys
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))
    
def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0 으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시(이미 최단 거리라면 무시)
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)
# test