# 백준 10250번 문제 - ACM호텔
test_data = int(input())
for i in range(test_data):
    h, w, n = map(int, input().split())
    f = 0 
    hotel = 0 
    if n % h == 0:
        f = h*100
        hotel = n // h
    else:
        f = (n % h) * 100
        hotel = 1 + n // h
    print(f+hotel)
