# 백준 3052번 문제 - 나머지
n = 42
cnt = 0
res = []
num_list = []
for i in range(3):
    num_list.append(int(input()))
print(num_list)
for i in num_list:
    res.append((str(i%42)))
    rest = res.count(str(i))
    print("result: ",rest)
    if rest>=2:
        continue
    else:
        cnt+=1
    print("cnt: ",cnt)
print(cnt)
