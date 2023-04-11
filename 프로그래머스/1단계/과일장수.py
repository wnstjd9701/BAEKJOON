# 프로그래머스 1단계 - 과일 장수 
def solution(k, m, score):
    answer = 0
    score.sort()
    l = len(score)
    box = []
    for i in range(0, l // m):
        if  l-(i+1)*3 < 0:
            break
        box = score[l-(i+1)*m:l-(i*m)]
        print(box)
        answer += box[0] * len(box)
    
    
    return answer
print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))
print(solution(4,3,	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))