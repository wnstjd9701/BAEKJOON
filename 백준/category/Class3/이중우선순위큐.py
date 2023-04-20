# 백준 7662번 문제 - 이중 우선순위 큐
import sys
import heapq
input = sys.stdin.readline


test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    visit = [0] * 1_000_001

    n = int(input())

    for i in range(n):
        cmd = input().split()
        if cmd[0] == 'I':
            heapq.heappush(min_heap, (int(cmd[1]), i))
            heapq.heappush(max_heap, (int(cmd[1]) * -1, i))
            visit[i] = 1 #True이면 어떤 힙에서도 아직 삭제되지 않은 상태

        elif cmd[0] == 'D':
            if cmd[1] == '-1': #삭제연산시, key값을 기준으로 해당 노드가 다른힙에서 삭제된 노드인가를 먼저 판단한다.
                # 이미 상대힙에 의해 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 계쏙 버리다가 이후 삭제대상노드가 나오면 삭제한다.
                while min_heap and not visit[min_heap[0][1]]: # visit이 False일떄 -> 해당노드가 삭제된상태
                    heapq.heappop(min_heap) # 버림 (상대힙에서 이미 삭제된노드이므로)
                if min_heap:
                    visit[min_heap[0][1]] = 0 # visit이 Ture엿으므로 False로 바꾸고 내가 삭제함
                    heapq.heappop(min_heap)
            elif cmd[1] == '1':
                while max_heap and not visit[max_heap[0][1]]: #이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)

    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')