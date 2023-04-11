# 프로그래머스 1단계 - 명예의 전당
def solution(k, score):
    answer = []
    rank = []
    l = len(score)
    for i in range(l):
        if i < k:
            rank.append(score[i])
            rank.sort(reverse=True)
            answer.append(rank[-1])
            continue
        if rank[k-1] < score[i]:
            rank.append(score[i])
            rank.sort(reverse=True)
            rank.pop()
            answer.append(rank[-1])
        else:
            answer.append(rank[-1])
    return answer
print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))

q = []
ans = []
score = [10,100,20,150,1,100,200]
k = 3
for s in score:
    q.append(s)
    if(len(q)>k):
        q.remove(min(q))
    ans.append(min(q))
print(ans)