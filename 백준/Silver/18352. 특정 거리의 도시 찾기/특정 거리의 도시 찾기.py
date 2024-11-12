from collections import deque
import sys
input = sys.stdin.readline

def BFS(K, X):
    # 최단 거리 탐색
    queue = deque()
    queue.append(X)  # 시작점
    visited[X] = 1
    cnt = 0

    while queue:
        if cnt == K:
            # return start
            break
        else:
            cnt += 1

        for i in range(len(queue)):
            start = queue.popleft()

            for next_city in tree_list[start]:
                if visited[next_city] == 0:
                    visited[next_city] = 1
                    queue.append(next_city)

    answer = list(queue)
    if not answer:
        answer.append(-1)
    return sorted(answer)

N, M, K, X = map(int, input().split())
# input_list = [list(map(int, input().split())) for _ in range(M)]

# 이동 여부를 기록할 배열
# visited = [[0]*(M) for _ in range(M)]
visited = [0] * (N+1)       # 인덱스 값을 맞추기 위해 N+1로 구현
tree_list = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    tree_list[A].append(B)

print(*BFS(K, X), sep="\n")
