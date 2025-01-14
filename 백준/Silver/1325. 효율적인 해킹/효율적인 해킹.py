# 효율적인 해킹

from collections import deque

def BFS(start):
    queue = deque()
    queue.append(start)

    visited = [0] * (N + 1)
    visited[start] = 1
    cnt = 0

    while queue:
        # 노드 위치, 횟수
        x = queue.popleft()

        # for j in range(1, N+1):
        for j in board[x]:
            # 각 노드에서 연결된 노드를 찾아서 횟수와 함께 큐에 넣기
            if visited[j] == 0:
                visited[j] = 1
                # queue.append((j, cnt + 1))
                queue.append(j)
                cnt += 1

    return cnt


N, M = map(int, input().split())
input_list = [list(map(int, input().split())) for _ in range(M)]

# 인접 리스트 생성
# board = [[0]*(N+1) for _ in range(N+1)]
board = [[] for _ in range(N+1)]
for i in range(M):
    board[input_list[i][1]].append(input_list[i][0])

answer_list = []
max_cnt = 0

for start in range(1, N+1):
    cnt = BFS(start)

    if max_cnt < cnt:
        max_cnt = cnt
        answer_list = [start]
    elif max_cnt == cnt:
        answer_list.append(start)

# for ans in answer_list:
    # print(ans, end = ' ')

print(*sorted(answer_list))