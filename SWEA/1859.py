# 1859. 백만 장자 프로젝트 D2
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    price = price[::-1]
    length = len(price)
    max_val = price[0]
    result = 0

    for i in range(1, length):
        if max_val > price[i]:
            result += max_val - price[i]
        else:
            max_val = price[i]
    
    print("#{} {}".format(test_case, result))