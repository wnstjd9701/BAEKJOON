# 프로그래머스 2단계 - 2018월간 코드 챌린지1 - 이진 변환 반복하기
def solution(s):
    answer = []
    countZero = 0 # 제거된 0의 개수
    countBinary = 0 # 이진 변환 횟수
    while True:
        if s == '1':
            break
        
        countBinary += 1

        countZero += s.count('0')
    
        s = s.replace('0', '')

        newLength = len(s)

        s = bin(newLength)[2:]
    return [countBinary, countZero]