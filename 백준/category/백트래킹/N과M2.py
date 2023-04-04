# 백준 15650번 문제 - N 과 M (2)
N, M = map(int, input().split())
visited = [0 for _ in range(N)]
arr = []

def dfs(cnt):
    if cnt == M:
        print(*arr)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1  # 중복 제거
            arr.append(i+1)

            dfs(cnt+1)  # 다음 깊이 탐색
            arr.pop()  # 탐사한 내용 제거

            # 순열 부분과의 차이점
            for j in range(i+1, N):
                visited[j] = 0

dfs(0)


from itertools import combinations

N, M = map(int, input().split())

p = combinations(range(1, N+1), M)
for i in p:
    print(*i)
