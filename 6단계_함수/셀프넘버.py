# 백준 4673번 문제 - 셀프 넘버
def d(n):
    a = 0
    for x in list(str(n)):
        a = a + int(x) 
    return int(n) + a
a= []
for i in range(1,10001):
    k = d(i)
    a.append(k)

for b in range(1, 10001):
    if b in a:
        continue # or pass
    else:
        print(b)