# 백준 1427번 문제 - 소트인사이드
n = list(input())
n.sort(reverse=True)
new_list = "".join(n)
print(new_list)

