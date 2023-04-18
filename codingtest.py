# 코딩테스트
def main():
    import sys
    t = int(sys.stdin.readline().strip())
    result = []
    for k in range(t):
        n = int(sys.stdin.readline().strip())
        answer = 0
        graph = [list(map(str, sys.stdin.readline().strip().split())) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    x, y = i, j
        horizonal, vertical = "",""
        for i in range(n):
            horizonal += graph[x][i]
            vertical += graph[i][y]
    
        for s in horizonal.split('Y'):
            if 'X' in s and 'HH' in s:
                answer += s.count('HH')
    
        for s in vertical.split('Y'):
            if 'X' in s and 'HH' in s:
                answer += s.count('HH')
        # res = '#{} {}'.format(k+1, answer)
        result.append(answer)
    for i in range(len(result)):
        print('#{} {}'.format(i+1, result[i]))

if __name__ == '__main__':
    main()