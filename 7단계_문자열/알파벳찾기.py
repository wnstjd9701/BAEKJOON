# 백준 10809번 문제 - 알파벳 찾기 
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet:
    print(word.find(chr(x)))    # find 함수 - 문자열에서만 사용가능, 문자가 문자열에 포함되지 않은경우 -1 반환