# 프로그래머스 1단계 - 크레인 인형뽑기 게임
def solution(board, moves):
    stack_list = []
    answer = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                stack_list.append(board[i][move-1])
                board[i][move-1] = 0
            
                if len(stack_list) > 1:
                    if stack_list[-1] == stack_list[-2]:
                        stack_list.pop(-1)
                        stack_list.pop(-2)
                        answer += 2
                break
    return answer