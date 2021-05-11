# 백준 1110번 문제 - 더하기 사이클
n = int(input())
check = n
new_num = 0
temp = 0
count = 0
while True:
    temp = n//10 + n%10
    new_num = (n%10)*10 + temp%10
    count += 1
    n = new_num
    if new_num == check:
        break
print(count)