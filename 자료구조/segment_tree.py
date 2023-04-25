# Segment Tree Data Structure
n = int(input())
arr = []
segment_tree = [0] * (n*4)
def init(start, end, index):
    if start == end:
        segment_tree[index] = arr[start-1]
        return segment_tree[index]
    mid = (start + end) // 2
    segment_tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2 + 1)
    return segment_tree[index]

def find(start, end, index, left, right):
    if start > right or end > left:
        return 0
    
    if start >= left and end <= right:
        return segment_tree[index]
    
    mid = (start + end) // 2
    sub_sum = find(start, mid, index*2, left, right) + find(mid+1, end, index*2 + 1, left, right)
    return sub_sum

def update(start, end, index, update_idx, update_data):
    if start > update_idx or end < update_idx:
        return
    segment_tree[index] += update_data
    
    mid = (start + end) // 2
    update(start, mid, index*2, update_idx, update_data)
    update(mid+1, end, index*2 + 1, update_idx, update_data)
