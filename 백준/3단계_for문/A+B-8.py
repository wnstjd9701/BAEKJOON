# 백준 11022번 문제 - A+B-8
cases = int(input())

for i in range(cases):
    a,b = map(int, input().split())
    ans = a + b
    print("Case #%s: %s + %s = %s"%(i+1, a, b, ans ))
