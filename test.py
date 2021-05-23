arr = []
index = 0
for i in range(2,10001):
    arr.append(str(i))
arr = list(map(int,arr))

for i in range(2,101):
    mul = 1
    while i*mul <= 10000:
        if i*mul in arr:
            if i*mul>=2 and i*mul<=100:
                arr
            else:
                arr.remove(i*mul)
        mul+=1   
print(arr)