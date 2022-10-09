# 프로그래머스 2단계 - 완전탐색 - 카펫
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for weight in range(total, 2, -1):
        if total % weight == 0: # 약수인 경우
            height = total // weight # 가로 * 세로 = total
            if yellow == (weight - 2) * (height - 2): # yellow 값이 같은 경우
                return [weight, height]