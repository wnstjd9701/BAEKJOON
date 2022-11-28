# 백준 11060번 문제 - 점프 점프
import collections
n=int(input())
arr=list(map(int, input().split()))
dp=[1e9 for _ in range(n)]
def bfs():
    q=collections.deque()
    q.append((0, 0))
    dp[0]=0
    while q:
        cur, cnt=q.popleft()
        if arr[cur]==0:
            continue
        for i in range(1, arr[cur]+1):
            nxt=cur+i
            if 0<=nxt<n and dp[nxt]>cnt+1:
                dp[nxt]=cnt+1
                q.append((nxt, cnt+1))
bfs()
if dp[n-1]==1e9:
    dp[n-1]=-1
print(dp[n-1])