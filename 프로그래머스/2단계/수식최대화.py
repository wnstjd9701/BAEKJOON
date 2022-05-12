# 프로그래머스 2단계 - 2020 카카오 인턴쉽 - 수식 최대화
def solution(expression):
    operator = ['*', '+', '-']
    result = []
    for i in operator:
        result.append(expression.split(i))
    for o in result:
        
    # 1. * + -
    # 2. * - +
    # 3. - + *
    # 4. - * +
    # 5. + - *
    # 6. + * -
    answer = 0
    
    return answer
