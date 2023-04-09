# 프로그래머스 2단계 - 할인 행사
from collections import Counter
def solution(want, number, discount):
    answer = 0
    d = dict()

    for i in range(len(want)):
        d[want[i]] = number[i]
    
    #num = sum(number)
    # 어차피 최대 10이기 때문에 굳이 구할필요없이 10으로 둬도 된다. 
    for i in range(len(discount) - 9): # 인덱스 범위 조심
        if d == Counter(discount[i:i+10]):
            answer += 1
    return answer
print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))