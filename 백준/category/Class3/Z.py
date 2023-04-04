# 백준 1074번 문제 - Z
import sys
n, r, c = map(int, input().split())
def z(n,r,c,q):
    if n == 0:
        return q
    half = 2**(n-1) # 한 변의 절반 길이
    if r < half: # 1사분면
        if c < half: # 1사분면
            quad = 0
        else: # 2사분면
            # 앞에 1개의 사각형이 존재 
            quad = 1
            # 빼주는 이유는 2사분면이 1사분면이 되기 때문에 2사분면이면
            # 왼쪽으로 이동하기 때문에 (2**(n-1)이동)이동하는 만큼 빼준다.
            c -= half 
    else:
        if c < half: # 3사분면
            # 앞에 2개의 사각형이 존재
            quad = 2
            # 3사분면은 위로 이동하기 때문에 행(r)을 빼준다. 
            r -= half
        else: # 4사분면
            # 앞에 3개의 사각형이 존재하기 때문
            quad = 3
            # 4사분면은 왼쪽, 위로 이동하기 때문에 행(r), 열(c)를 빼준다.
            r -= half
            c -= half
    # 앞에 존재하는 사각형 * (개수)
    q += (quad) * half**2
    return (z(n-1,r,c,q))

print(z(n,r,c,0))

