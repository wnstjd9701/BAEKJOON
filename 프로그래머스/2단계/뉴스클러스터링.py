# [Programmers] [KAKAO BLIND RECRUITMENT] [Python] Level2_[1차] 뉴스 클러스터링
from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    new_str1 = []
    new_str2 = []

    for i in range(1, len(str1)):
        if str1[i].isalpha() and str1[i-1].isalpha():
            new_str1.append(str1[i-1] + str1[i])
    for j in range(1, len(str2)):
        if str2[j].isalpha() and str2[j-1].isalpha():
            new_str2.append(str2[j-1] + str2[j])
    Counter1 = Counter(new_str1)
    Counter2 = Counter(new_str2)

    intersection = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(intersection) == 0:
        return 65536
    return int(len(intersection) / len(union) * 65536)
print(solution('aa1+aa2', 'AAAA12'))

# [Programmers] [KAKAO BLIND RECRUITMENT] [Python] Level2_[1차] 뉴스 클러스터링
def solution2(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    new_str1 = []
    new_str2 = []
    intersection = [] # 교집합
    union = [] # 합집합

    for i in range(1, len(str1)):
        if str1[i].isalpha() and str1[i-1].isalpha():
            new_str1.append(str1[i-1] + str1[i])
    for j in range(1, len(str2)):
        if str2[j].isalpha() and str2[j-1].isalpha():
            new_str2.append(str2[j-1] + str2[j])
    
    for string in new_str1:
        if string in new_str2:
            intersection.append(string)
            union.append(string)
            new_str2.remove(string)
        else:
            union.append(string)
    for k in range(len(new_str2)):
        union.append(new_str2[k])
    
    if len(union) == 0 and len(intersection) == 0:
        return 65536
    return int((len(intersection) / len(union)) * 65536)
print(solution2('aa1+aa2', 'AAAA12'))