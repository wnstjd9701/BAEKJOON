# 백준 1543번 문제 - 문서 검색
s = input()
search_s = input()
l = len(search_s)
idx = 0
answer = 0
while True:
    if idx + l > len(s):
        break
    if s[idx:idx + l] == search_s:
        idx += l
        answer += 1
    else:
        idx += 1
print(answer)