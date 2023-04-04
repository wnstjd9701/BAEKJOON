# 백준 9461번 문제 - 파도반 수열
n = int(input())
d = [0 for _ in range(101)]

for _ in range(n):
    d[0],d[1],d[2],d[3],d[4] = 1,1,1,2,2
    p = int(input())
    for i in range(5, p):
        d[i] = d[i-5] + d[i-1]
    print(d[p-1])
