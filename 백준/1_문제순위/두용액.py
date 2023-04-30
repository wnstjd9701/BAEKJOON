# 백준 2470번 문제 - 두 용액
n = int(input())
arr = sorted(list(map(int, input().split())))

left = 0
right = n-1

answer = abs(arr[left] + arr[right])
check = [arr[left], arr[right]]


while left < right:
    s = arr[left] + arr[right]
  
    if abs(s) < answer:
        answer = abs(s)
        check = [arr[left], arr[right]]
        if answer == 0:
          break
    if s < 0:
        left += 1
    else:
        right -= 1

print(check[0], check[1])