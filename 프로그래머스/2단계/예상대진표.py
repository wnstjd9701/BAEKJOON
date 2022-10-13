# 프로그래머스 2단계 - 2017 팁스타운 - 예상 대진표
def solutino(n,a,b):
    answer = 0 
    newA, newB = 0, 0
    cnt = 1
    if a < b: # A가 B보다 작을 경우 
        while a <= 1:
            if a % 2 == 0: # A가 짝수일 경우
                cnt += 1
                newA = a / 2
                if b % 2 == 0: # B가 짝수일 경우
                    newB = b / 2
                else:
                    newB = b / 2 + 1
                sub = newB - newA
                if sub == 1 and newA % 2 == 1 and newB % 2 == 0:
                    break
            else:
                newA = a / 2 + 1
                if b % 2 == 0:
                    newB = b / 2
                else: 
                    newB = b / 2 + 1        
    else: # A가 B보다 클 경우

    return answer