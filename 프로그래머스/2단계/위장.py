# 프로그래머스 2단계 - 위장
def solution(clothes):
    answer = 1
    dic = {}
    for v, k in clothes:
        if not k in dic: # 처음일 경우 딕셔너리 초기화
            dic[k] = 0
        dic[k] += 1
    
    for v in dic.values():
        answer *= v + 1
    
    return answer - 1 
    