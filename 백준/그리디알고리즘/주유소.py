# 백준 13305번 문제 - 주유소
n = int(input())
distance = list(map(int, input().split()))
costs = list(map(int, input().split()))

res = distance[0] * costs[0]
m = costs[0]
dist = 0
for i in range(1, n-1):
    if costs[i] < m: 
        res += m * dist
        dist = distance[i]
        m = costs[i]
    else:
        dist += distance[i]

    if i == n-1:
        res += m * dist
        
print(res)

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

res = 0
m = costs[0]
for i in range(n-1):
    if costs[i] < m:
        m = costs[i]
    res += m * roads[i]

print(res)
