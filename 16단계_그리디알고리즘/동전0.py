# 백준 11047번 문제 - 그리디 알고리즘
n, k = map(int, input().split())
coin_list = []
for i in range(n):
    coin_list.append(int(input()))

# 동전 내림차순 정렬
coin_list.sort(reverse=True)

# 동전의 개수 셀 변수 
count = 0

# 동전 개수 구하기
for coin in coin_list:
    if k==0: break
    val = k//coin # 몫 = 동전의 개수 
    count += val # 동전의 개수 더해주기
    k = k%coin # 나머지 값 k에 저장
print(count) # 필요한 동전의 최소 개수 
# greedy algorithm
