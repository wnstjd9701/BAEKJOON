# 프로그래머스 2단계 - 2019 카카오 개발자 겨울 인턴십 - 튜플
def solution(s):
    answer = []
    s_list = list(map(int, s.replace("{", "").replace("}", "").split(",")))
    
    number = {}
    for i in s_list:
        if i not in number:
            number[i] = 1
        else:
            number[i] += 1
    
    snum = sorted(number.items(), key=lambda x:x[1], reverse=True)
    for k in snum:
        answer.append(k[0])
    
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")