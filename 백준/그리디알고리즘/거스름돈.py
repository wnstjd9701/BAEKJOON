# 백준 5585번 문제 - 거스름돈
n = int(input())
val = 1000 - n
# 500, 100, 50, 10, 5, 1
coin = [500, 100, 50, 10, 5, 1]
count = 0
for i in coin:
    count += (val // i)
    val = val % i
print(count)


