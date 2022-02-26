from collections import defaultdict
user_list_who_i_report = defaultdict(set) # 신고를 한 유저 목록 ( set )
num_of_reported = defaultdict(int) # 유저가 신고 당한 횟수 ( int )
be_reported = ['muzi','frodo','apeach','con']
for i in be_reported:
    num_of_reported[i] += 1
    user_list_who_i_report[i].add(i)
    print(num_of_reported)
    print(user_list_who_i_report)