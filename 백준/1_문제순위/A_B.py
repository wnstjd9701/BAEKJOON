# 백준 16953번 문제 - A -> B
from collections import deque
def solution(a, b):
    q = deque([(a,1)])
    while q:
        a, cnt = q.popleft()
        if a == b:
            print(cnt)
            return
        if a*2 <= b:
            q.append((a*2, cnt+1))
        if a*10+1 <= b:
            q.append((a*10+1, cnt+1))
    print(-1)

a, b = map(int, input().split())
solution(a,b)
    
    
# Heapq를 이용하여 
# 그리디 알고리즘을 사용한 풀이
import sys
import heapq

input = sys.stdin.readline
a , b = map(int,input().split())

def mulTwo(a, count):
    return count+1, a*2

def addOne(a, count):
    return count+1, int(str(a)+"1")

def solution(a, b):
    q = [(0, a)]
    while q:
        cnt, a = heapq.heappop(q)
        if a<b:
            heapq.heappush(q, mulTwo(a, cnt))
            heapq.heappush(q, addOne(a, cnt))
        elif a==b:
            return cnt+1
        else:
            continue
    return -1

print(solution(a, b))
