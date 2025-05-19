# 1966. 프린터 큐

import sys
input = sys.stdin.readline

from collections import deque

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))

    queue = deque([(q, i) for i, q in enumerate(input_list)])
    cnt = 0

    while queue:
        current = queue.popleft()

        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            cnt += 1
            if current[1] == M:
                print(cnt)
