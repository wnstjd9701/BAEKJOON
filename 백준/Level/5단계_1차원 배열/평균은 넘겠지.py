# 백준 4344번 문제 - 평균은 넘겠지
n = int(input())
for i in range(n):
    number = list(map(int, input().split()))
    avg = sum(number[1:])/number[0] # number[0] => 학생 수
    cnt = 0
    for score in number[1:]:
        if score>avg:
            cnt+=1
    rate = cnt/number[0]*100
    print(f'{rate:.3f}%')
