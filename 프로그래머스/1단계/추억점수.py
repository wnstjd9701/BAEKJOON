# 프로그래머스 1단계 - 추억 점수
def solution(name, yearning, photo):
    answer = []
    d = {}
    for i in range(len(name)):
          d[name[i]] = yearning[i]
    for i in range(len(photo)):
        res =0 
        for j in range(len(photo[i])):
            if photo[i][j] in d:
                res += d[photo[i][j]]
        answer.append(res)
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"],[11, 1, 55],[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may"],["kein", "deny", "may"], ["kon", "coni"]]))
