# 백준 15652번 문제 - N과 M(4)
from itertools import combinations_with_replacement

n,m=map(int,input().split())
numlist=map(str,range(1,n+1))
setlist=list(combinations_with_replacement(numlist,m))
print('\n'.join(list(map(' '.join,setlist))))

n, m = map(int, input().split())

s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)