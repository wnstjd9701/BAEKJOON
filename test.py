# Test
def print_fibonacci_up_to_n():
    a, b, n = map(int, input().split())
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

# 40 이하까지의 피보나치 수 출력
print_fibonacci_up_to_n()
