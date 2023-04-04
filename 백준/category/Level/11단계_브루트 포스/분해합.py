# 백준 2231번 문제 - 분해합
n = int(input())

divide_list = [0,1,10,100,1000,10000,100000,1000000]
arr = []

for i in range(1, n):
    next_num_list = [i]
    temp_num = i
    for j in range(len(str(i)),0,-1):
        if temp_num == 0:
            break
        next_num_list.append(temp_num // divide_list[j])
        temp_num = temp_num % divide_list[j]
    if sum(next_num_list) == n:
        arr.append(i)

if arr:
    print(arr[0])
else:
    print(0)