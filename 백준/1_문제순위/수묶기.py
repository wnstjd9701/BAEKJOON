# ?? 1744? ?? - ? ??
n = int(input())

minus_list = []
plus_list = []
one_list = []
answer = 0
for i in range(n):
    num = int(input())
    if num <= 0:
        minus_list.append(num)
    elif num > 1:
        plus_list.append(num)
    else:
        one_list.append(num)
plus_list.sort(reverse=True)
minus_list.sort()

len_plus = len(plus_list)
len_minus = len(minus_list)

if len_plus % 2 == 1: # ??? ?? 
    answer += plus_list[-1]
    for j in range(0, len_plus-1, 2):
        answer += plus_list[j] * plus_list[j+1]
else:
    for j in range(0, len_plus, 2):
        answer += plus_list[j] * plus_list[j+1]

if len_minus % 2 == 1:
    answer += minus_list[-1]
    for j in range(0, len_minus-1, 2):
        answer += minus_list[j] * minus_list[j+1]
else:
    for j in range(0, len_minus, 2):
        answer += minus_list[j] * minus_list[j+1]
    
for i in one_list:
    answer += i

print(answer)