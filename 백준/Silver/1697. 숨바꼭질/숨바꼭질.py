# 1697. 숨바꼭질
import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((N, 0))
    visited[N] = True

    while queue:
        loc, time = queue.popleft()

        if loc == K:
            return time

        # x-1로 이동, x+1로 이동, *2 이동
        if 0 <= loc*2 <= 100000 and not visited[loc*2]:
            visited[loc*2] = True
            queue.append((loc * 2, time + 1))
        if 0 <= loc - 1 <= 100000 and not visited[loc - 1]:
            visited[loc - 1] = True
            queue.append((loc - 1, time + 1))
        if 0 <= loc + 1 <= 100000 and not visited[loc + 1]:
            visited[loc + 1] = True
            queue.append((loc + 1, time + 1))

N, K = map(int, input().split())

visited = [False] * 100001
answer = bfs()

print(answer)