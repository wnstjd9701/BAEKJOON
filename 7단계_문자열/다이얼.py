# 백준 5622번 문제 - 다이얼
word = input().lower()
dial = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
time = 0
for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            time += dial.index(j) + 3

print(time)

