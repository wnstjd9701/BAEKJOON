# 프로그래머스 2단계 - 그리디 - 구명보트
from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True)) # deque 선언

    while len(people) > 1:
        if people[0] + people[-1] <= limit: # 제일 가벼운 사람과 제일 무거운 사람이 같이 탈 경우
            answer += 1
            people.pop() # 가벼운 사람 pop
            people.popleft() # 무거운 사람 popleft
        else: # 무거운 사람 혼자 탈 경우
            answer += 1
            people.popleft()
    if people:
        answer += 1
    
    return answer

# solution 2
def solution2(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer