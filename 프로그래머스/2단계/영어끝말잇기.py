def solution(n, words):
    history = [words[0]]
    for i in range(1, len(words)):
        
        # 한 글자인 단어는 인정되지 않습니다.
        if len(words[i]) == 1:    
            return [(i % n) + 1, (i + n) // n]
        else:
            
            # 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
            if words[i-1][-1] != words[i][0]:     
                return [(i % n) + 1, (i + n) // n]
            else:
                
                # 이전에 등장했던 단어는 사용할 수 없습니다.
                if words[i] in history:
                    return [(i % n) + 1, (i+n) // n]
                else:
                    history.append(words[i])

    return [0, 0]