# 백준 1181번 문제 - 단어 정렬
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로
import sys
n = int(sys.stdin.readline().strip())
words = []
for _ in range(n):
    words.append(sys.stdin.readline().strip())
new_words = set(words) # 중복 제거
words = list(new_words)
words.sort() # 사전 순으로 정렬
words.sort(key=len) 
for i in words:
    print(i)

