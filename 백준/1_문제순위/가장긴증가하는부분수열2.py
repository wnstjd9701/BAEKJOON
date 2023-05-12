# 백준 12015번 문제 - 가장 긴 증가하는 부분 수열
n = int(input())
arr = list(map(int, input().split()))
stack = [0]
def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if stack[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in arr:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[binary_search(i, 0, len(stack) - 1)] = i
print(len(stack) - 1) # 0을 빼야하므로 -1
