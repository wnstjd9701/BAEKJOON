T = 10
for test_case in range(1, T+1):
    dump = int(input())
    box = list(map(int, input().split()))
    
    for j in range(dump):
        high = max(box)
        low = min(box)

        high_index = box.index(max(box))
        low_index = box.index(min(box))
        
        box[high_index] -= 1
        box[low_index] += 1

    result = max(box) - min(box)
    print("#{} {}".format(test_case, result))