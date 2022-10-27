# 백준 2751번 문제 - 수 정렬하기 2
n = int(input())
num = [] # list

for _ in range(n):
    x = int(input())
    num.append(x) # 추가 
for i in sorted(num):
    print(i) # 출력