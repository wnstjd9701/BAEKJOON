# Greedy Algorithm - 거스름돈
n = 1260
count = 0
coin_list = [500,100,50,10]
for coin in coin_list:
    count += n // coin
    n %= coin
print(count)
