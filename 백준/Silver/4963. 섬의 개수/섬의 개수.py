from collections import deque

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def BFS(i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1


while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0]*w for _ in range(h)]
    answer = 0

    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and board[i][j] == 1:
                visited[i][j] = 1
                BFS(i, j)
                answer += 1

    print(answer)
