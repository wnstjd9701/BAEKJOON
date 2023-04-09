# 프로그래머스 2단계 - 피로도
from itertools import permutations
from collections import deque
def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0 
        
        for need, spend in p:
            if tmp >= need:
                tmp -= spend
                cnt += 1
        answer = max(answer, cnt)
    return answer
solution(80, [[80,20],[50,40],[30,10]])

#Backtracking
answer = 0
def dfs(k, cnt, dungeons, visited):
    global answer 
    if cnt > answer:
        answer = cnt
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False
        
def solution2(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer

# BFS
def solution3(k, dungeons):
    answer = -1
    queue = deque()
    queue.append((k, []))

    while queue:
        k, route = queue.popleft()
        for i in range(len(dungeons)):
            a, b = dungeons[i]
            if k >= a and i not in route:
                temp = route + [i]
                queue.append((k - b, temp))
            else:
                answer = max(answer, len(route))

    return answer