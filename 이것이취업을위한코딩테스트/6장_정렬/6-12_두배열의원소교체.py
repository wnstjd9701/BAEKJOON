# 두 배열의 원소 교체
n, k = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

arr_A.sort() # 배열 A는 오름차순 정렬 수행
arr_B.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    if arr_A[i] < arr_B[i]:
        arr_A[i], arr_B[i] = arr_B[i], arr_A[i]
    else:   # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(arr_A))