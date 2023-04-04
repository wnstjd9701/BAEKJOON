# 백준 1654번 문제 - 랜선 자르기
import sys
k, n = map(int, sys.stdin.readline().split())
lan = []
for _ in range(k):
    lan.append(int(sys.stdin.readline()))
start = 1
end = max(lan)

while(start <= end):
    mid = (start+end) // 2
    cnt = 0
    for i in lan:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1 
print(end)
