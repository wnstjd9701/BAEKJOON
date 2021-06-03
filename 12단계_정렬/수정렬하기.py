# 백준 2750번 문제 - 수 정렬하기

n = int(input())
arr_list = []
for i in range(n):
    num = int(input())
    arr_list.append(num)
arr_list.sort()
for num in arr_list:
    print(num)
