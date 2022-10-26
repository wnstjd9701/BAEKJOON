# 백준 2108번 문제 - 통계학
import sys
from collections import Counter
n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
# 산술평균
print(round(sum(num)/n)) 

# 중앙값
num.sort()
print(num[n//2])  

# 최빈값
cnt_li = Counter(num).most_common()
if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1]: # 최빈값이 2개 이상일 경우
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])

# 범위 
print(max(num) - min(num))
    