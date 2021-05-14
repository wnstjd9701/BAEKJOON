# 백준 2941번 문제 - 크로아티아 알파벳
croatia = input()
alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
for check in alphabet:
    croatia = croatia.replace(check, '*')
print(len(croatia))