from collections import deque

# 상하좌우 이동
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
INF = 10**6

# BFS를 통해 각 지점에서 다른 지점까지의 최단 거리를 계산하는 함수
def BFS_shortPath(start, num):
    y, x = start
    visited = [[0] * M for _ in range(N)]
    dq = deque([(y, x, 0)])

    while dq:
        y, x, d = dq.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = 1
        if room[y][x] == "*":
            n1 = numdict[(y, x)]
            graph[num][n1] = graph[n1][num] = d
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and room[ny][nx] != "x":
                dq.append((ny, nx, d + 1))

# DFS를 통해 최소 거리를 탐색하는 함수
def DFS(now, distance, cnt):
    global result
    if distance >= result:
        return
    if cnt == num:
        result = min(result, distance)
        return
    for next in range(1, num + 1):
        if not visited[next]:
            visited[next] = 1
            DFS(next, distance + graph[now][next], cnt + 1)
            visited[next] = 0

while True:
    M, N = map(int, input().split())
    if not N:
        break

    room = [list(input().strip()) for _ in range(N)]

    numdict = {}
    dirty = {}
    num = 0
    for y in range(N):
        for x in range(M):
            if room[y][x] == "o":
                robot = (y, x)
            elif room[y][x] == "*":
                num += 1
                numdict[(y, x)] = num
                dirty[num] = (y, x)

    result = INF
    graph = [[INF] * (num + 1) for _ in range(num + 1)]
    BFS_shortPath(robot, 0)
    
    for i in range(1, num + 1):
        if graph[0][i] == INF:
            result = -1
            break
    if result == -1:
        print(-1)
        continue

    for i in range(1, num + 1):
        BFS_shortPath(dirty[i], i)

    visited = [0] * (num + 1)
    DFS(0, 0, 0)
    print(result)
