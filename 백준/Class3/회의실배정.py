# 백준 1931번 문제 - 회의실 배정
n = int(input())
time = []
for _ in range(n):
    start, end = map(int, input().split()) 
    time.append([start,end])
time.sort(key = lambda x: x[0]) # 시작 시간을 기준으로 오름차순 정렬
time.sort(key = lambda x: x[1]) # 끝나는 시간을 기준으로 오름차순 정렬
last = 0 # 회의 마지막 시간 저장
count = 0 # 회의 개수 저장

for i, j in time:
    if i>=last: # 시작시간이 회의의 마지막 시간보다 크거나 같은 경우
        count += 1
        last = j
print(count)