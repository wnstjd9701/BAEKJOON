# 백준 10816번 문제 - 숫자 카드2
from collections import Counter
n = int(input())
card_n = list(map(int, input().split()))
m = int(input())
card_m = list(map(int, input().split()))

card_n = Counter(card_n)
for i in card_m:
    print(card_n[i], end=' ')
            
