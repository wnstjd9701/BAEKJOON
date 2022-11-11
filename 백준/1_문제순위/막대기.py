# 백준 1094번 문제 - 막대기
x = int(input())
arr = [64,32,16,8,4,2,1]
count = 0

for i in range(len(arr)):
    if x>=arr[i]:
        count += 1
        x -= arr[i]
    if x == 0:
        break
print(count)

    

    
    
    