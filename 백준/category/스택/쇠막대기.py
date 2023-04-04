# 백준 10799번 문제 - 쇠막대기
a = list(input())
s = []
b = 0
for i in range(len(a)):
    if a[i] == '(':
        s.append('(')
    else:
        if a[i-1] == '(':
            s.pop()
            b = b+len(s)
        else:
            s.pop()
            b = b+1
print(b)