# 프로그래머스 2단계 - 2017팁스타운 - 짝지어 제거하기
def solution(s):
    stack = []

    for i in s:
        if not stack: # stack이 비어있을 경우 stack에 push
            stack.append(i)
        elif stack[-1] == i: # stack의 마지막 원소와 s에서 pop되는 원소가 같은 경우
            stack.pop()
        else: # stack의 마지막 원소와 pop되는 원소가 다른 경우 그 원소를 stack에 추가
            stack.append(i)
    
    if len(stack) > 0:
        return 0
    else:
        return 1