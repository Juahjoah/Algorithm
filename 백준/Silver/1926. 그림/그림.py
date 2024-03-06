from collections import deque

# 입력 값을 input으로 받기
n, m = map(int, input().split())
inputArr = [list(map(int, input().split())) for _ in range(n)]

def BFS_corrected():
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    answerCnt = 0  # 총 그림 개수
    maxAnswer = 0  # 가장 큰 그림 넓이

    def BFS(i, j):
            # 0이거나, 이미 방문한 경우를 제외하기
            if inputArr[i][j] == 0:
                return 0
            # 아닌 경우에 대한 값
            queue = deque()
            queue.append((i, j))
            inputArr[i][j] = 0  # 방문한 경우 제외하기
            answerArea = 1  # 그림의 넓이

            # queue를 돌면서 확인하기
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and inputArr[nx][ny] == 1:
                        inputArr[nx][ny] = 0  # 방문한 경우 처리
                        queue.append((nx, ny))
                        answerArea += 1
            return answerArea

    for i in range(n):
        for j in range(m):
            if inputArr[i][j] == 1:
                answerCnt += 1
                maxAnswer = max(maxAnswer, BFS(i, j))

    print(answerCnt)
    print(maxAnswer)


BFS_corrected()