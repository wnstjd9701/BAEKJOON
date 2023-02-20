# 백준 1300번 문제 - K번째 수
n, k = int(input()), int(input())
start, end = 1, k

while start <= end:
    mid = (start+end) // 2

    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)
    
    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
