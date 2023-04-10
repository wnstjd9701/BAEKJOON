# 프로그래머스 1단계 - 삼총사
def solution(number):
    tot = 0
    def dfs(i, depth, sum_num):
        nonlocal tot

        if depth == 3 and sum_num == 0:
            tot += 1
            return

        if i == len(number):
            return

        if depth < 3:
            dfs(i+1, depth+1, sum_num + number[i])
            dfs(i+1, depth, sum_num)

    dfs(0,0,0)        

    answer = tot


    return answer

def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt
print(solution([-2, 3, 0, 2, -5]))