# 프로그래머스 2단계 - 오픈채팅방
from collections import defaultdict
def solution(record):
    answer = []
    result = []
    user_id = defaultdict(str)
    for s in record:
        cmd = s.split()
        command = cmd[0]
        id = cmd[1]
        if command == 'Enter':
            user_id[id] = cmd[2]
            result.append([id, '님이 들어왔습니다.'])
        elif command == 'Leave':
            result.append([id, '님이 나갔습니다.'])
        elif command == 'Change':
            user_id[id] = cmd[2]
    for id, mention in result:
        if mention == '님이 들어왔습니다.':
            answer.append(user_id[id] + mention)
        else:
            answer.append(user_id[id] + mention)
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
