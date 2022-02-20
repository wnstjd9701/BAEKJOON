def binary_search(array, target, start, end):
   while start <= end: 
        mid = (start + end) // 2
        if mid == target:
            return mid
        elif mid < target:
            start = mid + 1
        else:
            end = mid - 1
        # elif mid > target:
        #   end = mid - 1
        # else:
        #   start = mid + 1
        
   return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('Nothing')
else:
    print(result + 1)
