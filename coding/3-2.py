# 이것이 취업을 위한 코딩테스트 - 큰 수의 법칙
n, m, k = map(int, input().split()) # n: 배열의 크기, m: m번 더하기, k: k번 까지 더할 수 있음
data_list = map(int, input().split()) # 동전 입력

data_list.sort() # 정렬
first = data_list[n-1]  # 기징 큰 수 
second = data_list[n-2] # 두 번째로 큰 수 
result = 0
while True:
    for i in range(k):  # 가장 큰 수를 k번 더하기 
        if m == 0:
            break
        result += first # 가장 큰 수 더하기 k번 반복
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)

# 수학적 접근
n, m, k = map(int, input().split()) # n: 배열의 크기, m: m번 더하기, k: k번 까지 더할 수 있음
data = list(map(int, input().split()))

data.sort()
first = data[n-1]   
second = data[n-2]

count = int(m / (k+1)) * k  # () 반복
count += m % (k+1)

result = 0
result += (count) * first   # 가장 큰 수 더하기 
result += (m-count) * second    # 두 번째로 큰 수 더하기

print(result)   # 최종 답안 출력
