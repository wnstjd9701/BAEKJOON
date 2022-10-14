# 프로그래머스 2단계 - [1차] 캐시 
from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0: return 5 * len(cities)
    answer = 0
    cache = deque(maxlen=cacheSize)
    for city in cities:
        city = city.upper()

        if city in cache: # cahce hit
            cache.remove(city)
            cache.append(city)
            answer += 1
        else: # cache miss
            cache.append(city)
            answer += 5

    return answer

solution(5, ["hi", "Hello", "test"])