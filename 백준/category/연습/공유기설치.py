# 백준 2110번 문제 - 공유기 설치
import sys
input = sys.stdin.readline
n, c = map(int, input().split())
x = []
for _ in range(n):
    x.append(int(input()))
x.sort()

def binary_search(x, start, end):
    while start <= end:
        mid = (start+end) // 2
        cur = x[0]
        cnt = 1
        for i in range(1, len(x)):
            if x[i] >= cur + mid:
                cnt += 1
                cur = x[i]
                print('current: ', cur)

        if cnt >= c:
            global result
            start = mid + 1
            result = mid
        else:
            end = mid - 1

start = 1
end = x[-1] - x[0]
result = 0

binary_search(x,start,end)
print(result)

