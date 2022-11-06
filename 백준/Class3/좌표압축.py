# 백준 18870번 문제 - 좌표 압축
n = int(input())
x = list(map(int, input().split()))
new_x = list(sorted(set(x)))

dict = {new_x[i]: i for i in range(len(new_x))}

for i in x:
    print(dict[i], end=" ")