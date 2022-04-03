# 프로그래머스 1단계 - 최소 직사각형
def solution(sizes):
    w_list = []
    h_list = []
    answer = 0
    temp = 0
    for i in range(len(sizes)):
        if sizes[i][0] <= sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    for i in range(len(sizes)):
        w_list.append(sizes[i][0])
        h_list.append(sizes[i][1])
    w = max(w_list)
    h = max(h_list)
    answer = w * h
    return answer

