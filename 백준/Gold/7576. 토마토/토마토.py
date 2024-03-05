
from collections import deque

# 입력 값을 input으로 받기
M, N = map(int, input().split())
inputArr = [list(map(int, input().split())) for _ in range(N)]

# 배열을 확인하기 위한 값
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# answerArr = inputArr

def BFS():
    days = -1            # 최소 일수를 계산하기
    queue = deque()

    # 최초 익은 토마토 (1) 값 추가하기
    for i in range(N):
        for j in range(M):
            if inputArr[i][j] == 1:
                queue.append((i, j))
    # queue를 돌면서 확인하기
    while queue:
        days += 1 # 날짜를 하나씩 추가하기
        for _ in range(len(queue)):
            x, y = queue.popleft()  # 같은 노드에 있는 작업을 한 번에 수행하기

            # 토마토 익히기
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and inputArr[nx][ny] == 0 :
                    inputArr[nx][ny] = 1
                    queue.append((nx,ny))

    # 모든 토마토가 익었는지 마지막으로 확인하기
    for k in range(N) :
        for l in range(M):
            if inputArr[k][l] == 0:
                return -1   # 안 익은 토마토가 존재하는 경우
    return days

# 함수 실행 및 최소 일수 출력하기
print(BFS())

