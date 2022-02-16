# # 백준 1541번 문제 - 잃어버린 괄호
exp = input().split("-")
ans = 0
for i in exp[0].split("+"):
    ans += int(i)

for i in exp[1:]:
    for j in i.split("+"):
        ans -= int(j)

print(ans)


# a = input().split('-')
# num = []
# for i in a:
#     cnt = 0
#     s = i.split('+')
#     for j in s:
#         cnt += int(j)
#     num.append(cnt)
# n = num[0]
# for i in range(1, len(num)):
#     n -= num[i]
# print(n)