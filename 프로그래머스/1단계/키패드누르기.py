# 프로그래머스 1단계 - 키패드 누르기
def solution(numbers, hand):
    answer = ''
    left_hand_location = 10
    right_hand_location = 12
    for i in numbers: 
        if i in [1,4,7]:
            answer += "L"
            left_hand_location = i
        elif i in [3,6,9]:
            answer += "R"
            right_hand_location = i
        else:
            i = 11 if i == 0 else i 
            dis_left = abs(left_hand_location - i)
            dis_right = abs(right_hand_location - i)
        
            if sum(divmod(dis_left, 3)) > sum(divmod(dis_right, 3)):
                answer += "R"
                right_hand_location = i
            elif sum(divmod(dis_left, 3)) < sum(divmod(dis_right, 3)):
                answer += "L"
                left_hand_location = i
            else:
                if hand == 'left':
                    answer += "L"
                    left_hand_location = i
                else:
                    answer += "R"
                    right_hand_location = i
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
