from collections import deque

# 네 방향 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def BFS(n, m, grid):
    # 목표 지점 찾기
    target_x, target_y = None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                target_x, target_y = i, j
                break
        if target_x is not None:
            break

    # BFS를 위한 큐 초기화
    queue = deque([(target_x, target_y)])
    distances = [[-1] * m for _ in range(n)]  # 모든 지점의 거리를 -1로 초기화
    distances[target_x][target_y] = 0  # 목표 지점의 거리는 0

    # BFS 실행
    while queue:
        x, y = queue.popleft()

        # 네 방향으로 이동
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            # 범위 내에 있고, 갈 수 있는 땅(1)이라면
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))

    # 결과 출력 준비
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:  # 원래 갈 수 없는 땅은 0으로 출력
                print(0, end=' ')
            else:
                print(distances[i][j], end=' ')
        print()


# 입력 처리
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
BFS(n, m, grid)
