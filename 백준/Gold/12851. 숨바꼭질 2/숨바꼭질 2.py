import sys
input = sys.stdin.readline

from collections import deque

def bfs(N, K):
    queue = deque()
    queue.append((N, 0))
    visited = [[0, 0] for _ in range(100001)] # [개수, 시간]
    visited[N][0] += 1

    while queue:
        node, time = queue.popleft()

        if node == K:
            return time, visited[node][0]

        for cur_node in [node + 1, node - 1, node * 2]:
            if 0 <= cur_node <= 100000:
                if visited[cur_node][1] == time + 1:            # 내가 이후에 방문해야 할 노드라면
                    visited[cur_node][0] += visited[node][0]    # 기존의 이동 값을 넣어줌.
                elif visited[cur_node][1] == 0:
                    visited[cur_node][0] += visited[node][0]
                    visited[cur_node][1] = time + 1
                    queue.append((cur_node, time + 1))

N, K = map(int, input().split())

answer, result = bfs(N, K)
print(answer)
print(result)
