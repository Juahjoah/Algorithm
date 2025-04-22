# 11725. 트리의 부모 찾기

from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = True

    while queue:
        node = queue.popleft()

        for n in adj_list[node]:
            if not visited[n]:
                answer_list[n] = node
                queue.append(n)
                visited[n] =True

    return


N = int(input())
input_list = [list(map(int, input().split())) for _ in range(N-1)]

adj_list = [[] for _ in range(N + 1)]

for x, y in input_list:
    adj_list[x].append(y)
    adj_list[y].append(x)

answer_list = [0] * (N + 1)
visited = [False] * (N + 1)
bfs()

for answer in range(2, N + 1):
    print(answer_list[answer])