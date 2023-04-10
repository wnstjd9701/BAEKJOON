# 백준 11656번 문제 - 접미사 배열
s = input()
a = []
for i in range(len(s)):
    a.append(s[i:i+len(s)])
a.sort()
for string in a:
    print(string)
