# 포 움직이기
def move_pho(horse_list):
    horse = horse_list
    check_x = []
    cnt = 0
    for i in range(n-1):
        s = horse[i] + horse[i+1] 
        if s == 'HH':
            cnt += 1
        elif horse[i] == 'Y': # Y를 만났을 때 
            if len(check_x) < 1 and cnt >= 1: # X가 없는데 Y를 만났고 COUNT가 1보다 크면 HH가 이전에 나온 것이므로 
                cnt = 0
            elif check_x: # X가 이미  있고 Y를 만났으면 종료
                break
        elif horse[i] == 'X':
            check_x.append('X')
    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    graph = [list(map(str, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                x, y = i, j
    horizonal_list, vertical_list = [], []
    for i in range(n):
        horizonal_list.append(graph[x][i])
        vertical_list.append(graph[i][y])
    answer = move_pho(horizonal_list) + move_pho(vertical_list)
    print(answer)