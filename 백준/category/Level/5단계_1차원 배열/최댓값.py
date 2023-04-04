# 백준 2562번 문제 - 최댓값
num = []
for i in range(9):
    num.append(int(input()))
print(max(num))
print(num.index(max(num))+1)