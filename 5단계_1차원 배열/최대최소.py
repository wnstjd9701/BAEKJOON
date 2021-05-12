# 백준 10818번 문제 - 최소,최대
Case = int(input())
num_list = list(map(int, input().split()))
print('{} {}'.format(min(num_list), max(num_list)))