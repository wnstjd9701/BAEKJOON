# 프로그래머스 구현 - 문자열 압축
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[:step] # 앞에서부터 step만큼 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하단면 압축 횟수(count) 증가
            if prev == s[j:j+step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer
