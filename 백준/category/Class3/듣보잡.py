# 백준 1764번 문제 - 듣보잡
import sys
n, m = map(int, sys.stdin.readline().split())
people_n, people_m = set(), set()

for _ in range(n):
    people_m.add( sys.stdin.readline().strip())
for _ in range(m):
    people_m.add(sys.stdin.readline().strip())
    
answer = sorted(list(people_n & people_m))

print(len(answer))
for i in range(len(answer)):
    print(answer[i])