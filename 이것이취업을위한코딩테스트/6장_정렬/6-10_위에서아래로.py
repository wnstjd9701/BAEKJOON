# 위에서 아래로 
n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

num.sort(reverse=True)
# num = num.sorted(num, reverse = True)
# sort 는 반환 값이 있고 sorted는 반환값이 없다.
# 따라사 sorted를 사용하려면 변수에 값을 넣어줘야 한다.  
for i in num:
    print(i, end=' ') 