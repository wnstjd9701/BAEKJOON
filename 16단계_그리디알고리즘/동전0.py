# 백준 11047번 문제 - 그리디 알고리즘
n, k = map(int, input().split())
coin_list = []
for i in range(n):
    coin = int(input())
    coin_list.append(coin)

coin_list.sort(reverse=True)

count = 0
for coin in coin_list:
    if k==0: break
    val = k//coin
    count += val
    k = k%coin
print(count)
print(coin_list)