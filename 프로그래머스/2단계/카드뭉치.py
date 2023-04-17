# 프로그래머스 2단계 - 카드 뭉치
from collections import deque 
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for i in range(len(goal)):
        if cards1 and cards1[0] == goal[i]:
            cards1.popleft()
        elif cards2 and cards2[0] == goal[i]:
            cards2.popleft()
        else:
            return "No"
    return "Yes"

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))