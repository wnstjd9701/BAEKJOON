# 백준 17413번 문제 - 단어 뒤집기 2
s = list(input())
tag = False
word = ''
result = ''
for i in s:
    if tag == False:
        if i == '<':
            tag = True
            word = word + i
        elif i == ' ':
            word = word + i
            result = result + word
            word = ''
        else:
            word = i + word # Point - 앞에 i를 더해준다.
    
    elif tag == True:
        word = word + i
        if i == '>':
            tag = False
            result = result + word
            word = ''
print(result + word)

            
        
        


