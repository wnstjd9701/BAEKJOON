# 백준 14891번 문제 - 톱니바귀
import sys
input = sys.stdin.readline

graph = []
for _ in range(4):
    graph.append(list(input().rstrip()))
k = int(input())
data = []

def rotate_clock(graph):
    temp = graph[7]
    for i in range(6, -1, -1):
        graph[i+1] = graph[i]
    graph[0] = temp

def rotate_reverse_clock(graph):
    temp = graph[0]
    for i in range(7):
        graph[i] = graph[i+1]
    graph[7] = temp

def dfs(x, y):
    global visited
    if visited[x] == 0:
        visited[x] = 1
        left = graph[x][6]
        right = graph[x][2]
        if y == 1: # clock
            rotate_clock(graph[x])
        else:
            rotate_reverse_clock(graph[x])
        if x-1 >= 0 and left != graph[x-1][2]:
            dfs(x-1, -y)
        if x+1 <= 3 and right != graph[x+1][6]:
            dfs(x+1, -y)
for _ in range(k):
    a, b = map(int, input().split())
    visited = [0] * 4
    dfs(a-1, b)

cnt = 0
for i in range(4):
    if graph[i][0] == '1':
        cnt += (2**i)

print(cnt)