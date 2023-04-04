# 백준 2630번 문제 - 색종이 만들기
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = []

def solution(x, y, n):
    half = n // 2
    color = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != graph[i][j]: # 하나라도 다르다면
                solution(x,y,half)
                solution(x,y+half,half)
                solution(x+half,y,half)
                solution(x+half,y+half,half)
                return
    # 모두 같은 색인 경우
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0,0,n)
print(result.count(0))
print(result.count(1))