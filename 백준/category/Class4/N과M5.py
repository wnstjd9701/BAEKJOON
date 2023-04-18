# 백준 15654번 문제 - N과 M(5)
from itertools import permutations

n, m = map(int, input().split())
new_list = list(map(int, input().split()))
new_list = sorted(new_list) #순서대로 나오게 정렬 먼저

for numbers in list(permutations(new_list, m)):
    for num in numbers:
        print(num, end=' ')
    print()