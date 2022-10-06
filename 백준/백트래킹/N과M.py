# 백준 15649번 문제 - N과 M(1)
n, m = map(int, input().split())

s = []
def solution():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if i in s:
            continue
        s.append(i)
        solution()
        s.pop()

solution()
