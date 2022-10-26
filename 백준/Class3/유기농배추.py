# 백준 1012번 문제 - 유기농 배추
t = int(input()) #테스트케이스의 개수

dx = [0,0,-1,1] # 상, 하, 좌, 우
dy = [1,-1,0,0]

def BFS(x,y):           
    queue = [(x,y)]
    cabbage[x][y] = 0 # 방문처리

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if cabbage[nx][ny] == 1 :
                queue.append((nx,ny))
                cabbage[nx][ny] = 0

# 행렬만들기
for i in range(t):
    m, n, k = map(int,input().split())
    cabbage = [[0]*(n) for _ in range(m)]
    cnt = 0

    for j in range(k):
        x,y = map(int, input().split())
        cabbage[x][y] = 1

    for a in range(m):
        for b in range(n):
            if cabbage[a][b] == 1:
                BFS(a,b)
                cnt += 1

    print(cnt)



# import sys 
# sys.setrecursionlimit(10000) 

# def dfs(x, y): 
# 	dx = [1, -1, 0, 0] 
# 	dy = [0, 0, 1, -1] 
    
#     # 상,하,좌,우 확인 
# 	for i in range(4): 
# 		nx = x + dx[i] 
#         ny = y + dy[i] 
        
#         if (0 <= nx < N) and (0 <= ny < M): 
#         	if matrix[nx][ny] == 1: 
#             	matrix[nx][ny] = -1 
#                 dfs(nx, ny)
               
# T = int(input()) 
# for _ in range(T): 
# 	M, N, K = map(int, input().split()) 
#     matrix = [[0]*M for _ in range(N)] 
#     cnt = 0 
    
#     # 행렬 생성 
#     for _ in range(K): 
#     	m, n = map(int, input().split()) 
#     	matrix[n][m] = 1 
        
#     for i in range(N): # 행 (바깥 리스트) 
#     	for j in range(M): # 열 (내부 리스트) 
#         	if matrix[i][j] > 0: 
#             	dfs(i, j) 
#                 cnt += 1 
# print(cnt)