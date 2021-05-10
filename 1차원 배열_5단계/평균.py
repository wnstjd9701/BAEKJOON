# 백준 1546번 문제 - 평균
n = int(input())
exam_list = list(map(int, input().split()))
max_score = max(exam_list)

for i in range(n):
    exam_list[i] = exam_list[i]/max_score*100
print(sum(exam_list)/n)


#n = int(input())  # 과목 수
#test_list = list(map(int, input().split()))
#max_score = max(test_list)

#new_list = []
#for score in test_list :
#    new_list.append(score/max_score *100)  # 새로운 점수 생성
#test_avg = sum(new_list)/n
#print(test_avg)