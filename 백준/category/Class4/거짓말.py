# 백준 1043번 문제 - 거짓말
import sys
n, m = list(map(int, sys.stdin.readline().split()))
truth = list(map(int, sys.stdin.readline().split()))[1:]

KNOW_TRUTH = 0
parent = [i for i in range(n + 1)]
for person in truth:
    parent[person] = KNOW_TRUTH

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parties = []
for _ in range(m):
    party = list(map(int, sys.stdin.readline().split()))[1:]
    for i in range(len(party) - 1):
        union(party[i], party[i + 1])
    parties.append(party)

answer = 0
for party in parties:
    know = False
    for i in range(len(party)):
        if find(party[i]) == KNOW_TRUTH:
            know = True
            break
    if not know:
        answer += 1

print(answer)
                