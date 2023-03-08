def solution(stats):
    answer = 0
    stack = [[0] for _ in range(len(stats))]
    for i in range(len(stats)):
        if i == 0:
            stack[i][0] = stats[i]
        for j in range(i):
            if i >= j:
                if stack[j][0] < stats[i]:
                    stack[j][0] = stats[i]
                    break
                elif stack[j][0] == 0:
                    stack[j][0] = stats[i]
                    break
                elif stack[j][0] > stats[i]:
                    continue
    for s in stack:
        if s[0] > 0:
            answer += 1
   
    return answer
print(solution([5,3,4,6,2,1]))
print(solution([6,2,3,4,1,5]))