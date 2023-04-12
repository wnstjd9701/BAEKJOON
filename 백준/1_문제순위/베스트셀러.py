# 백준 1302번 문제 - 베스트셀러
n = int(input())
book = {}
for _ in range(n):
    name = input()
    if name not in book:
        book[name] = 0
    book[name] += 1        
print(sorted(list(book.items()), key=lambda x : (-x[1],x[0]))[0][0])