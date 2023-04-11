# 프로그래머스 2단계 - 전화번호 목록
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        s = ""
        for number in phone_number:
            s += number
            print(s)
            if s in hash_map and s != phone_number:
                return False
    return True
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))