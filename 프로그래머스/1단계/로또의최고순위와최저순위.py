# 프로그래머스 1단계 - 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = [0,0]
    rank = [6,6,5,4,3,2,1]
    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    answer = rank[cnt_0 + ans], rank[ans]
    return answer