# 프로그래머스 1단계 - 신고 결과 받기
from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    report = set(report)

    user_report = defaultdict(set) # 신고를 한 유저 목록 ( set )
    user_num_of_reported = defaultdict(int) # 유저가 신고 당한 횟수 ( int )
    suspended = []

    for r in report:
        do_report, be_reported = r.split()
        
        user_num_of_reported[be_reported] += 1
        user_report[do_report].add(be_reported)
        
        if user_num_of_reported[be_reported] == k:
            suspended.append(be_reported)
        
    for s in suspended:
        for i in range(len(id_list)):
            if s in user_report[id_list[i]]:
                answer[i] += 1
    return answer
    
ans = solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
print(ans)