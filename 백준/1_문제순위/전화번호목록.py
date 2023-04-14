# 백준 5052번 문제 - 전화번호 목록
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    phone_book = [str(sys.stdin.readline().strip()) for _ in range(n)] # 전화번호를 문자열로 받는다.
    phone_book.sort() # 오름차순으로 정렬하여 사전순으로 정렬
    check = "YES" # 일관성이 있는지 체크
    print(phone_book)
    # 반복문을 통해 전화번호를 확인
    for i in range(len(phone_book) - 1):
        # 현재 전화번호의 문자열과 다음 전화번호의 현재 전화번호 길이만큼의 문자열과 같은지 확인
        # 같으면 일관성이 없는 것
        if phone_book[i] == phone_book[i + 1][0:len(phone_book[i])]:
            check = "NO"
    print(check)    