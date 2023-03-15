# 백준 11000번 문제 - 강의실 배정
import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    schedule_list = [list(map(int, input().split())) for _ in range(n)]
    schedule_list.sort()

    room_queue = list()
    heapq.heappush(room_queue, schedule_list[0][1])

    for i in range(1, n):
        if schedule_list[i][0] >= room_queue[0]:
            heapq.heappop(room_queue)
        heapq.heappush(room_queue, schedule_list[i][1])
    
    print(len(room_queue))
