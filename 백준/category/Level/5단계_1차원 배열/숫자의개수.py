# 백준 2577번 문제 - 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
result = list(str(A*B*C))
# result 에 ['1','2','3','4','5','6','7'] 이런식으로 저장이 됨
for i in range(10):
    print(result.count(str(i)))