# 백준 1744번 문제 - 수 묶기
n = int(input())

minus_list = []
plus_list = []
one_list = []
answer = 0

for i in range(n):
    num = int(input())
    if num > 1:
        plus_list.append(num)
    elif num <= 0:
        minus_list.append(num)
    else:
        one_list.append(num)

plus_list.sort(reverse=True)
minus_list.sort()

if len(plus_list)%2 == 1:
    answer += plus_list[-1]
    for j in range(0, len(plus_list)-1, 2):
        answer += plus_list[j] * plus_list[j+1]
else:
    for j in range(0, len(plus_list), 2):
        answer += plus_list[j] * plus_list[j+1]

if len(minus_list)%2 == 1:
    answer += minus_list[-1]
    for j in range(0, len(minus_list)-1, 2):
        answer += (minus_list[j]) * (minus_list[j+1])
else:
    for j in range(0, len(minus_list), 2):
        answer += (minus_list[j]) * (minus_list[j+1])

for i in range(len(one_list)):
    answer += one_list[i]
    
print(answer)