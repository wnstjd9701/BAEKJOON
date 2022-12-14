# 백준 1449번 문제 - 수리공 항승
n, l = map(int, input().split())
d = list(map(int, input().split()))
d.sort()

end = 0 
index = 0
for i in d:
    if i > end:
        end = i + l - 1
        index += 1
print(index)