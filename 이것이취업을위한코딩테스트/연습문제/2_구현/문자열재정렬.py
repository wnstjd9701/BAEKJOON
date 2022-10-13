# 구현 - 문자열 재정렬
data = input()
# 구현 - 문자열 재정렬
s = input()
result = []
value = 0

for data in s:
    if data.isalpha():
        result.append(data)
    else:
        value += int(data)

result.sort()

if value != 0:
    result.append(str(value))
    
print("".join(result))