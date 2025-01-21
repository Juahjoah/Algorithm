from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(i, j):
    queue = deque()
    queue.append((i,j))

    cnt_S = 0
    cnt_W = 0

    while queue:
        x, y = queue.popleft()
        
        # 맨 처음 들어오는 값도 판단해주기 위해 양, 늑대를 nx, ny로 확인하지 않고 x,y로 확인
        if farm[x][y] == 'o':
            cnt_S += 1
        if farm[x][y] == 'v':
            cnt_W += 1

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and farm[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

    if cnt_S > cnt_W:
        cnt_W = 0
    else:
        cnt_S = 0

    return cnt_S, cnt_W


R, C = map(int, input().split())
farm = [list(input()) for _ in range(R)]

visited = [[False]*C for _ in range(R)]
answer_Sheep = 0
answer_Wolf = 0


for i in range(R):
    for j in range(C):
        if farm[i][j] != '#' and not visited[i][j] :
            sheep = 0
            wolf = 0
            visited[i][j] = 1

            sheep, wolf = bfs(i, j)

            answer_Sheep += sheep
            answer_Wolf += wolf

print(answer_Sheep, answer_Wolf)