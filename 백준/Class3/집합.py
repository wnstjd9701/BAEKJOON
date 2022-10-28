# 백준 11723번 문제 - 집합
import sys
s = set()
n = int(input())
for i in range(n):
    tmp = sys.stdin.readline().strip().split()

    if len(tmp) == 1: # tmp 길이가 1
        if tmp[0] == 'all': # all
                s = set([i for i in range(1,21)])
        else: # empty
            s = set()
        continue

    command, target = tmp[0], tmp[1]    
    target = int(target)    

    if command == 'add':    
        s.add(target)   
    elif command == 'check':    
        print(1 if target in s else 0)  
    elif command == 'remove':   
        s.discard(target)   
    elif command == 'toggle':   
        if target in s: 
            s.dicard(target)    
        else:   
            s.add(target)   
    