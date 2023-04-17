# 프로그래머스 2단계 - n진수 게임
def convert(n, base):
    arr = '0123456789ABCDEF'
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]
def solution(n, t, m, p):
    answer = ''
    conv = ''
    
    for i in range(t*m):
        conv += convert(i, n)

    for i in range(p-1, t*m, m):
        answer += conv[i]
        
    return answer
print(solution(2,4,2,1))