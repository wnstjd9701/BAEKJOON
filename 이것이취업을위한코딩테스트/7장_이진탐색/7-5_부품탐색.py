# 부품 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
req = list(map(int, input().split()))

for i in req:
    result = binary_search(arr, i, 0, n-1)
    if result == None:
        print('no')
    else:
        print('yes')