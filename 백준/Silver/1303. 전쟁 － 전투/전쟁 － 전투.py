from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def BFS(i, j):
    queue = deque()
    queue.append((i, j))

    cnt = 1                                                     # 숫자를 셀 때, 처음 들어 오는 값도 고려해야 하기 때문에 꼭 1로 두고 시작!

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and input_list[nx][ny] == input_list[i][j]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1

    return cnt


N, M = map(int, input().split())
input_list = [list(input()) for _ in range(M)]

visited = [[0]*N for _ in range(M)]
answer_W = 0
answer_B = 0

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and input_list[i][j] == 'W':
            # BFS(i, j)
            visited[i][j] = 1
            answer_W += BFS(i, j)**2
        elif visited[i][j] == 0 and input_list[i][j] == 'B':
            # BFS(i, j)
            visited[i][j] = 1
            answer_B += BFS(i, j)**2


print(answer_W, answer_B)


