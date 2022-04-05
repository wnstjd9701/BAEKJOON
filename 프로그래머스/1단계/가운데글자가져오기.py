# 프로그래머스 1단계 - 가운데 글자 가져오기
def solution(s):
    answer = ''
    length = len(s)
    if length % 2 == 0:
        answer = s[length//2-1:length//2+1]
    else:
        answer = s[length // 2]
    return answer

