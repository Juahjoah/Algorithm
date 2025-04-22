# 1260. DFS와 BFS
from collections import deque


def dfs(node):
    # 1. 스택 활용
    # 2. 재귀 활용

    # 해당 깊이의 노드를 방문 처리
    visited_dfs[node] = True
    answer_dfs.append(node)

    # 그 노드에 대한 for문
    for n in adj_list[node]:
        # 방문하지 않았다면, 해당 노드로 dfs 시작
        if not visited_dfs[n]:
            dfs(n)


def bfs():
    queue = deque()
    queue.append(V)
    visited_bfs[V] = True

    while queue:
        node = queue.popleft()

        answer_bfs.append(node)

        for n in adj_list[node]:
            if not visited_bfs[n]:
                queue.append(n)
                visited_bfs[n] = True



N, M, V = map(int, input().split())
input_list = [list(map(int, input().split())) for _ in range(M)]

adj_list = [[] for _ in range(N + 1)]

for x, y in input_list:
    adj_list[x].append(y)
    adj_list[y].append(x)

for a in adj_list:
    a.sort()

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

answer_dfs = []
answer_bfs = []

dfs(V)
bfs()

print(*answer_dfs)
print(*answer_bfs)