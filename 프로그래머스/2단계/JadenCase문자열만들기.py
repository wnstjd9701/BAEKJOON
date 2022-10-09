# 프로그래머스 2단계 - 연습문제 JadenCase 문자열 만들기
def solution(s):
    answer = ''
    words = s.split(' ')

    for i in range(len(words)):
        words[i] = words[i].capitalize()

    answer = ' '.join(words)
    
    return answer
