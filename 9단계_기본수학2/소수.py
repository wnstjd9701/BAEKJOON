# 백준 2581번 문제 - 소수
m, n = map(int, input().split())
sum_list = []
min_list = []
for i in range(m, n):
    for j in range(2,i):
        if i%j==0:
            print()
        else:
            if i in sum_list:
                print()
            else:
                sum_list.append(i)
print(sum_list)

