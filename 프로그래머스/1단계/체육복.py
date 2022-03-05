# 프로그래머스 1단계 - 체육복
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    print(_reserve)
    print(_lost)
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

def set_solution(n, lost, reserve):
    newlost = set(lost) - set(reserve)
    newreserve = set(reserve) - set(lost)
    for i in newlost:
        if i-1 in newreserve:
            newreserve.remove(i-1)
        elif i+1 in newreserve:
            newreserve.remove(i+1)
        else:
            n-=1
    return n

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
ans = solution(n, lost, reserve)