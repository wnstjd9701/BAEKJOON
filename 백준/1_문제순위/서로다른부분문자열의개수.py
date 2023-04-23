# 백준 11478번 문제 - 서로 다른 부분 문자열의 개수
string = input()
stack = set()
for i in range(len(string)):
    for j in range(i, len(string)):
        stack.add(string[i:j+1])
print(len(stack))