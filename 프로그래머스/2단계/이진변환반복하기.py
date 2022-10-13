# 프로그래머스 2단계 - 2018월간 코드 챌린지1 - 이진 변환 반복하기
def solution(s):
    answer = []
    countZero = 0 # 제거된 0의 개수
    countBinary = 0 # 이진 변환 횟수
    while True:
        if s == '1': # s가 1이 되었을때 중단
            break
        
        countBinary += 1 # 이진 변환을 하였으므로 +1

        countZero += s.count('0') # 이진수에 있는 0의 개수를 셈
    
        s = s.replace('0', '') # 0을 없애주기

        newLength = len(s) # 이진 변환된 수의 길이 저장

        s = bin(newLength)[2:] # 이진 변환하는 함수를 통해 0b~~로 나오므로 앞의 2개는 빼고 슬라이싱 

    return [countBinary, countZero] # 이진변환횟수, 없앤 0의 개수 